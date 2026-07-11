# OptiCrop Flowchart

The flow of the application is:

1. User submits soil and weather inputs on the homepage.
2. Flask receives the request at `/predict`.
3. The feature vector is scaled and passed to the trained ML model.
4. The model returns the recommended crop and confidence score.
5. Prediction details are stored in SQLite.
6. User can view history, dashboard, or download a PDF report.
