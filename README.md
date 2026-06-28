# OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is a production-ready Flask application that recommends the most suitable crop for a given set of soil and climate conditions. It combines a trained machine learning model with a clean web interface and reporting workflow for farmers, researchers, and agricultural planners.

## Features

- Intelligent crop prediction from soil and weather parameters
- Responsive web interface for form-based prediction
- Prediction history with CSV export
- PDF report generation for recommendations
- Dashboard with model comparison and recent predictions
- REST-style API endpoints for integration
- SQLite-backed storage for predictions and reports

## Screenshots

Add screenshots to the screenshots/ directory and reference them here once available.

## Tech Stack

- Backend: Python, Flask
- Machine Learning: scikit-learn, pandas, NumPy, joblib
- Database: SQLite, SQLAlchemy
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Deployment: Render, Gunicorn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/OptiCrop-Smart-Agricultural-Production-Optimization-Engine.git
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
4. Create a local environment file:
   ```bash
   copy .env.example .env
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Dataset

The project uses the crop recommendation dataset stored in [dataset/crop_recommendation.csv](dataset/crop_recommendation.csv).

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
models/
```

## API Endpoints

- GET /api/health — health check
- GET /api/history — recent predictions
- POST /api/predict — prediction endpoint

## Model Information

The model artifacts are stored as:
- model.pkl
- scaler.pkl
- label_encoder.pkl

If these files are missing, the app will train them automatically on first startup.

## Deployment

The repository includes deployment configuration for Render via [render.yaml](render.yaml) and [Procfile](Procfile).

## Future Scope

- Multi-language interface support
- Mobile app integration
- Advanced weather-based forecasting
- Farmer-specific recommendation insights

## License

This project is intended for educational and research purposes.

## Author

OptiCrop Team

