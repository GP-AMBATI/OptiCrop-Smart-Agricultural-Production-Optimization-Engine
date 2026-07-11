# OptiCrop ER Diagram

Entities:

- User: stores login and profile metadata
- Prediction: stores input parameters, predicted crop, and confidence
- Report: exports and stores PDF report metadata
- Dataset: dataset information and record counts
- MLModel: model metadata and performance tracking

Relationships:

- User -> Prediction: one-to-many
- Prediction -> Report: one-to-one
- Dataset -> MLModel: one-to-many
