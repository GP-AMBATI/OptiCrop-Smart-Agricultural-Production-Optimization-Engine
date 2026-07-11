import csv
import io
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import (Flask, flash, jsonify, make_response, redirect,
                   render_template, request, url_for)
from fpdf import FPDF

from database import (SessionLocal, User, Prediction, Report, init_db,
                      get_or_create_guest_user, log_prediction)
from model import (CROP_DETAILS, ensure_artifacts, get_crop_context,
                   get_model_comparison, load_artifacts, predict_crop)

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "development-secret-key")

ROOT = Path(__file__).resolve().parent
DATASET_PATH = ROOT / "dataset" / "crop_recommendation.csv"

ensure_artifacts()
model, scaler, encoder = load_artifacts()
model_metrics = get_model_comparison()

init_db()


def get_session():
    return SessionLocal()


@app.route("/")
def index():
    crop_samples = ["rice", "maize", "lentil", "watermelon"]
    return render_template(
        "index.html",
        title="OptiCrop | Smart Agricultural Production Optimization",
        crop_samples=crop_samples,
        model_metrics=model_metrics,
    )


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return redirect(url_for("index"))

    form_data = request.form if request.form else request.get_json(silent=True) or {}
    required_fields = ["n", "p", "k", "temperature", "humidity", "ph", "rainfall"]
    try:
        features = [float(form_data.get(field, "")) for field in required_fields]
    except ValueError:
        flash("Please enter valid numeric values for all input fields.", "danger")
        return redirect(url_for("index"))

    if any(value < 0 for value in features):
        flash("Input values must be non-negative.", "danger")
        return redirect(url_for("index"))

    crop_name, confidence, probabilities = predict_crop(model, scaler, encoder, features)
    crop_info = get_crop_context(crop_name)

    db = get_session()
    user = get_or_create_guest_user(db)
    prediction_record = log_prediction(
        db,
        user.user_id,
        features,
        crop_name,
        confidence,
        probabilities,
    )
    db.close()

    if request.is_json:
        return jsonify(
            {
                "crop": crop_name,
                "confidence": round(confidence * 100, 2),
                "crop_info": crop_info,
                "probabilities": probabilities,
                "prediction_id": prediction_record.id,
            }
        )

    return render_template(
        "result.html",
        title="OptiCrop Results",
        prediction=prediction_record,
        crop_info=crop_info,
        probabilities=probabilities,
        rounded_confidence=round(confidence * 100, 2),
    )


@app.route("/history")
def history():
    db = get_session()
    records = db.query(Prediction).order_by(Prediction.timestamp.desc()).all()
    db.close()

    if request.args.get("format") == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow([
            "Timestamp",
            "N",
            "P",
            "K",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall",
            "Predicted Crop",
            "Confidence",
        ])
        for row in records:
            writer.writerow([
                row.timestamp,
                row.n,
                row.p,
                row.k,
                row.temperature,
                row.humidity,
                row.ph,
                row.rainfall,
                row.predicted_crop,
                f"{row.confidence:.2%}",
            ])
        response = make_response(output.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=prediction_history.csv"
        response.headers["Content-Type"] = "text/csv"
        return response

    return render_template(
        "history.html",
        title="Prediction History",
        predictions=records,
    )


@app.route("/download")
def download():
    prediction_id = request.args.get("prediction_id")
    if not prediction_id or not prediction_id.isdigit():
        flash("Invalid prediction record selected for download.", "warning")
        return redirect(url_for("history"))

    db = get_session()
    record = db.query(Prediction).filter(Prediction.id == int(prediction_id)).first()
    db.close()

    if record is None:
        flash("Requested prediction not found.", "warning")
        return redirect(url_for("history"))

    crop_info = get_crop_context(record.predicted_crop)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 12, "OptiCrop Prediction Report", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(4)
    pdf.cell(0, 10, f"Prediction ID: {record.id}", ln=True)
    pdf.cell(0, 10, f"Date: {record.timestamp}", ln=True)
    pdf.ln(4)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Input Parameters:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"Nitrogen (N): {record.n}", ln=True)
    pdf.cell(0, 8, f"Phosphorus (P): {record.p}", ln=True)
    pdf.cell(0, 8, f"Potassium (K): {record.k}", ln=True)
    pdf.cell(0, 8, f"Temperature: {record.temperature} °C", ln=True)
    pdf.cell(0, 8, f"Humidity: {record.humidity} %", ln=True)
    pdf.cell(0, 8, f"pH: {record.ph}", ln=True)
    pdf.cell(0, 8, f"Rainfall: {record.rainfall} mm", ln=True)

    pdf.ln(6)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Recommendation:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"Crop: {record.predicted_crop.title()}", ln=True)
    pdf.cell(0, 8, f"Confidence: {record.confidence:.2%}", ln=True)
    pdf.cell(0, 8, f"Season: {crop_info.get('season')}", ln=True)
    pdf.cell(0, 8, f"Water Needs: {crop_info.get('water')}", ln=True)
    pdf.multi_cell(0, 8, f"Fertilizer Suggestion: {crop_info.get('fertilizer')}")

    pdf.ln(6)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Crop Notes:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, crop_info.get("description", "No details available."))

    pdf_output = pdf.output(dest="S").encode("latin-1")
    response = make_response(pdf_output)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = f"attachment; filename=OptiCrop_Report_{record.id}.pdf"
    return response


@app.route("/dashboard")
def dashboard():
    db = get_session()
    predictions = db.query(Prediction).order_by(Prediction.timestamp.desc()).limit(10).all()
    db.close()
    crop_counts = {}
    for row in predictions:
        crop_counts[row.predicted_crop] = crop_counts.get(row.predicted_crop, 0) + 1

    return render_template(
        "dashboard.html",
        title="OptiCrop Dashboard",
        crop_counts=crop_counts,
        model_metrics=model_metrics,
        selected_model=model_metrics.get("selected_model"),
        data_shape=model_metrics.get("data_shape"),
        recent_predictions=predictions,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About OptiCrop",
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Contact Us",
    )


@app.route("/api/health")
def api_health():
    return jsonify({"status": "ok", "service": "OptiCrop"})


@app.route("/api/history")
def api_history():
    db = get_session()
    records = db.query(Prediction).order_by(Prediction.timestamp.desc()).limit(50).all()
    db.close()
    data = [record.to_dict() for record in records]
    return jsonify(data)


@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():
    if request.method == "GET":
        query = request.args
    else:
        query = request.get_json(silent=True) or {}

    try:
        features = [
            float(query.get("n", 0)),
            float(query.get("p", 0)),
            float(query.get("k", 0)),
            float(query.get("temperature", 0)),
            float(query.get("humidity", 0)),
            float(query.get("ph", 0)),
            float(query.get("rainfall", 0)),
        ]
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid numeric input supplied."}), 400

    crop_name, confidence, probabilities = predict_crop(model, scaler, encoder, features)
    db = get_session()
    user = get_or_create_guest_user(db)
    record = log_prediction(db, user.user_id, features, crop_name, confidence, probabilities)
    db.close()

    return jsonify(
        {
            "status": "success",
            "crop": crop_name,
            "confidence": round(confidence * 100, 2),
            "probabilities": probabilities,
            "prediction_id": record.id,
        }
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", title="Page Not Found"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
