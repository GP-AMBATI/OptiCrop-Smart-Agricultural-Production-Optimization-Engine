# OptiCrop Smart Agricultural Production Optimization Engine

OptiCrop is a Flask-based crop recommendation platform that helps farmers and agricultural planners select the most suitable crop based on soil and environmental features. The application combines a trained machine learning model with a modern web interface, prediction history, and downloadable reports.

## Features

- Crop recommendation from soil and climate inputs
- Responsive web interface for real-time predictions
- Prediction history and CSV export
- PDF report generation for recommendations
- Dashboard with model metrics and recent predictions
- REST-style API endpoints for integration
- SQLite-backed storage for predictions and reports

## Tech Stack

- Backend: Python, Flask
- Machine Learning: scikit-learn, pandas, NumPy, joblib
- Database: SQLite, SQLAlchemy
- Frontend: HTML, CSS, JavaScript
- Deployment: Render, Gunicorn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OptiCrop-Smart-Agricultural-Production-Optimization-Engine.git
   cd OptiCrop-Smart-Agricultural-Production-Optimization-Engine
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the environment template and update values if needed:
   ```bash
   copy .env.example .env
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Dataset

The project uses the crop recommendation dataset stored in [dataset/crop_recommendation.csv](dataset/crop_recommendation.csv). The application also includes trained model artifacts for immediate use.

## How to Run

- Development server:
  ```bash
  python app.py
  ```
- Production server:
  ```bash
  gunicorn app:app
  ```

## Project Structure

```text
app.py
database.py
model.py
requirements.txt
README.md
.gitignore
.env.example
static/
templates/
dataset/
notebooks/
docs/
reports/
screenshots/
models/
```

## API Endpoints

- GET /api/health — health check
- GET /api/history — recent predictions
- POST /api/predict — prediction endpoint
- GET /history — web-based prediction history view
- GET /download — PDF report download

## Model Information

The trained artifacts are stored as:
- [model.pkl](model.pkl)
- [scaler.pkl](scaler.pkl)
- [label_encoder.pkl](label_encoder.pkl)

If these files are missing, the application will regenerate them on startup.

## Deployment

Deployment configuration is included for Render via [render.yaml](render.yaml) and [Procfile](Procfile).

## Future Scope

- Multi-language interface support
- Mobile application integration
- Weather-driven forecasting enhancements
- Farmer-specific advisory insights

## License

This project is intended for educational and research purposes.

## Author

OptiCrop Team

