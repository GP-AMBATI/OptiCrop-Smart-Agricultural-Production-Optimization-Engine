import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pandas as pd
import numpy as np
from joblib import dump, load
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False

ROOT = Path(__file__).resolve().parent
DATASET_PATH = ROOT / "dataset" / "crop_recommendation.csv"
MODEL_PATH = ROOT / "model.pkl"
SCALER_PATH = ROOT / "scaler.pkl"
ENCODER_PATH = ROOT / "label_encoder.pkl"

FEATURE_COLUMNS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

CROP_DETAILS: Dict[str, Dict[str, str]] = {
    "rice": {
        "description": "Rice is a high-yield cereal crop best grown in warm, wet climates.",
        "season": "Kharif",
        "water": "High water requirement",
        "fertilizer": "Balanced NPK with emphasis on nitrogen",
    },
    "maize": {
        "description": "Maize is a versatile crop used for food, feed, and industry.",
        "season": "Kharif",
        "water": "Moderate to high water need",
        "fertilizer": "Balanced NPK with potassium support",
    },
    "chickpea": {
        "description": "Chickpea is a nutritious pulse crop suited to semi-arid regions.",
        "season": "Rabi",
        "water": "Low to moderate water need",
        "fertilizer": "Phosphorus-rich fertilizer for early growth",
    },
    "kidneybeans": {
        "description": "Kidney beans are protein-rich pulses grown in well-drained soil.",
        "season": "Rabi",
        "water": "Moderate water need",
        "fertilizer": "Apply organic matter and moderate nitrogen",
    },
    "pigeonpeas": {
        "description": "Pigeon pea is a durable pulse crop for dry climates.",
        "season": "Kharif",
        "water": "Low to moderate water requirement",
        "fertilizer": "Use phosphorus and micronutrients",
    },
    "mothbeans": {
        "description": "Moth bean is a drought-tolerant pulse grown in arid areas.",
        "season": "Kharif",
        "water": "Very low water requirement",
        "fertilizer": "Light nitrogen with phosphorus support",
    },
    "mungbean": {
        "description": "Mung bean is a short-duration pulse crop with good soil-restoring ability.",
        "season": "Kharif",
        "water": "Low to moderate water need",
        "fertilizer": "Low nitrogen and balanced phosphorus",
    },
    "blackgram": {
        "description": "Black gram is a fast-growing legume used in many cuisines.",
        "season": "Kharif",
        "water": "Moderate water need",
        "fertilizer": "Phosphorus-rich application at planting",
    },
    "lentil": {
        "description": "Lentil is a cool-season pulse crop with a short growth cycle.",
        "season": "Rabi",
        "water": "Low water requirement",
        "fertilizer": "Low nitrogen and moderate phosphorus",
    },
    "coffee": {
        "description": "Coffee is a perennial crop grown in shaded, humid environments.",
        "season": "Year-round",
        "water": "Regular irrigation in dry periods",
        "fertilizer": "High organic matter and balanced NPK",
    },
    "cotton": {
        "description": "Cotton is a fiber crop that grows best in warm climates.",
        "season": "Kharif",
        "water": "Moderate water requirement",
        "fertilizer": "Balanced NPK with emphasis on potassium",
    },
    "grapes": {
        "description": "Grapes thrive in dry climate conditions with good drainage.",
        "season": "Rabi",
        "water": "Moderate water need",
        "fertilizer": "Balanced fertilizer with micronutrients",
    },
    "watermelon": {
        "description": "Watermelon is a summer fruit crop with high water demand.",
        "season": "Summer",
        "water": "High water requirement",
        "fertilizer": "Nitrogen-rich fertilizer during vegetative stage",
    },
    "muskmelon": {
        "description": "Muskmelon is a heat-loving fruit crop with fast growth.",
        "season": "Summer",
        "water": "High water need",
        "fertilizer": "Balanced NPK with extra potassium",
    },
    "apple": {
        "description": "Apple is a temperate fruit crop requiring cold dormancy.",
        "season": "Rabi",
        "water": "Moderate water with good drainage",
        "fertilizer": "Nitrogen and potassium for fruit development",
    },
    "orange": {
        "description": "Orange is a citrus fruit crop grown in subtropical climates.",
        "season": "Rabi",
        "water": "Moderate water requirement",
        "fertilizer": "Balanced fertilizer with micronutrients",
    },
    "banana": {
        "description": "Banana is a tropical fruit crop with heavy nutrient demand.",
        "season": "Year-round",
        "water": "High water requirement",
        "fertilizer": "High potassium and nitrogen fertilizer",
    },
    "papaya": {
        "description": "Papaya is a fast-growing tropical fruit crop.",
        "season": "Year-round",
        "water": "Moderate to high water need",
        "fertilizer": "Balanced NPK and calcium support",
    },
    "coconut": {
        "description": "Coconut palms thrive in humid tropical climates.",
        "season": "Year-round",
        "water": "Moderate to high water need",
        "fertilizer": "Balanced fertilizer with micronutrients",
    },
    "jute": {
        "description": "Jute is a fiber crop grown in warm, humid regions.",
        "season": "Kharif",
        "water": "Moderate water requirement",
        "fertilizer": "Nitrogen-rich fertilizer for vegetative growth",
    },
    "pomegranate": {
        "description": "Pomegranate is a drought-tolerant fruit crop with long lifespan.",
        "season": "Rabi",
        "water": "Low to moderate water need",
        "fertilizer": "Balanced fertilizer with phosphorus",
    },
}


def load_dataset(path: Path = DATASET_PATH) -> pd.DataFrame:
    """Load the crop recommendation dataset from the dataset directory."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {path}")
    df = pd.read_csv(path)
    return df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset by removing duplicates and missing rows."""
    current_shape = df.shape
    df = df.drop_duplicates().dropna().reset_index(drop=True)
    return df


def preprocess_data(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, StandardScaler, LabelEncoder]:
    """Prepare features and labels for training."""
    features = df[FEATURE_COLUMNS].astype(float)
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    encoder = LabelEncoder()
    y = encoder.fit_transform(df["label"].astype(str))
    return X, y, scaler, encoder


def build_models() -> Dict[str, Any]:
    """Create the set of candidate classification models."""
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, solver="lbfgs"),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=120, random_state=42),
        "KNN": KNeighborsClassifier(n_neighbors=7),
        "SVM": CalibratedClassifierCV(SVC(kernel="rbf", random_state=42), cv=3),
        "Naive Bayes": GaussianNB(),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    }
    if XGBOOST_AVAILABLE:
        models["XGBoost"] = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss", verbosity=0, random_state=42)
    return models


def evaluate_model(model: Any, X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray) -> Dict[str, Any]:
    """Train a model and return evaluation metrics."""
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, average="weighted", zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, average="weighted", zero_division=0)),
        "f1_score": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
        "classification_report": classification_report(y_test, y_pred, zero_division=0, output_dict=True),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
    }


def train_and_save() -> Tuple[str, Dict[str, Any]]:
    """Train multiple models, select the best one, and save artifacts."""
    df = clean_dataset(load_dataset())
    X, y, scaler, encoder = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    models = build_models()
    results: Dict[str, Any] = {}
    best_name = "Random Forest"
    best_score = 0.0
    best_model = None

    for name, model in models.items():
        metrics = evaluate_model(model, X_train, X_test, y_train, y_test)
        results[name] = metrics
        if metrics["accuracy"] > best_score:
            best_score = metrics["accuracy"]
            best_name = name
            best_model = model

    if best_model is None:
        best_name = "Random Forest"
        best_model = models["Random Forest"]
        best_model.fit(X_train, y_train)

    dump(best_model, MODEL_PATH)
    dump(scaler, SCALER_PATH)
    dump(encoder, ENCODER_PATH)
    results["selected_model"] = best_name
    results["data_shape"] = df.shape
    return best_name, results


def load_artifacts() -> Tuple[Any, StandardScaler, LabelEncoder]:
    """Load the trained model, scaler, and label encoder from disk."""
    if not MODEL_PATH.exists() or not SCALER_PATH.exists() or not ENCODER_PATH.exists():
        raise FileNotFoundError("Model artifacts are missing. Run train_and_save() first.")
    model = load(MODEL_PATH)
    scaler = load(SCALER_PATH)
    encoder = load(ENCODER_PATH)
    return model, scaler, encoder


def ensure_artifacts() -> None:
    """Generate model artifacts if they do not already exist."""
    if not MODEL_PATH.exists() or not SCALER_PATH.exists() or not ENCODER_PATH.exists():
        train_and_save()


def build_feature_vector(values: List[float]) -> pd.DataFrame:
    """Build a feature vector for prediction with the original column names."""
    return pd.DataFrame([values], columns=FEATURE_COLUMNS)


def predict_crop(model: Any, scaler: StandardScaler, encoder: LabelEncoder, raw_features: List[float]) -> Tuple[str, float, Dict[str, float]]:
    """Predict the best crop, confidence score, and class probabilities."""
    features = build_feature_vector(raw_features)
    scaled = scaler.transform(features)

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(scaled)[0]
    else:
        proba = np.zeros(len(encoder.classes_), dtype=float)

    prediction_idx = int(model.predict(scaled)[0])
    crop_label = encoder.inverse_transform([prediction_idx])[0]
    confidence = float(max(proba)) if proba.any() else 0.0
    proba_map = {encoder.inverse_transform([idx])[0]: float(value) for idx, value in enumerate(proba)}
    return crop_label, confidence, proba_map


def get_crop_context(crop_name: str) -> Dict[str, str]:
    """Return crop metadata for the recommendation page."""
    return CROP_DETAILS.get(crop_name.lower(), {
        "description": "Crop information is not available for this selection.",
        "season": "Seasonal data unavailable",
        "water": "Water requirements unavailable",
        "fertilizer": "Fertilizer suggestions unavailable",
    })


def get_model_comparison() -> Dict[str, Any]:
    """Return a summary of trained model performance for the dashboard."""
    df = clean_dataset(load_dataset())
    X, y, scaler, encoder = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    models = build_models()
    comparison: Dict[str, Any] = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        comparison[name] = {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred, average="weighted", zero_division=0)),
            "recall": float(recall_score(y_test, y_pred, average="weighted", zero_division=0)),
            "f1_score": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
        }

    return comparison
