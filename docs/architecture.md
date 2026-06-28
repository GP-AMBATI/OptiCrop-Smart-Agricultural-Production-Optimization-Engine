# OptiCrop Architecture

OptiCrop is built with a Flask backend that serves HTML pages and REST APIs. The ML pipeline is implemented in `model.py` and uses a trained model saved as `model.pkl`.

Key components:

- `app.py`: Flask routes, PDF export, prediction handling, API endpoints
- `model.py`: dataset loading, cleaning, feature scaling, training, model evaluation
- `database.py`: SQLite schema for users, predictions, reports, datasets, and ML models
- `templates/`: HTML templates built with Bootstrap 5
- `static/`: CSS and JavaScript assets for UI, charts, and interactivity
- `dataset/`: crop recommendation dataset file
