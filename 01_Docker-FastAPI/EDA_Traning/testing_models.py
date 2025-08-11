import pandas as pd
import joblib

# 1. Load the saved model
model = joblib.load("models/random_forest.joblib")

# 2. Prepare new raw data (same columns as training X)
# Note: Missing values are okay; pipeline will handle them
new_penguins = pd.DataFrame({
    "island": ["Torgersen", "Biscoe"],
    "bill_length_mm": [39.1, 46.0],
    "bill_depth_mm": [18.7, 14.9],
    "flipper_length_mm": [181.0, 230.0],
    "body_mass_g": [3750.0, 5850.0],
    "sex": ["male", "female"]
})

# 3. Make predictions
predictions = model.predict(new_penguins)
print("Predicted species:", predictions)

# Optional: Prediction probabilities
probs = model.predict_proba(new_penguins)
print("Prediction probabilities:\n", probs)