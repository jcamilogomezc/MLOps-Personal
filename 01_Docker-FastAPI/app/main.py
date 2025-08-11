from fastapi import FastAPI, HTTPException
from data_models import PredictRequest, PredictResponse
import pandas as pd
import joblib
import json

app = FastAPI(title="Penguin Species Prediction API", version="1.0", description="API for predicting penguin species using trained models.")


# Read the json file containing model paths
with open("models/models.json") as f:
    model_paths = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Penguin Species Prediction API, ACTUALIZADO!"}

# Server status
@app.get("/status")
def get_status():
    return {"status": "running", 
            "version": "1.0", 
            "Available models": list(model_paths.keys())}
# Predict endpoint
@app.post("/predict", response_model=PredictResponse)
def predict_species(request: PredictRequest) -> PredictResponse:
    try:
        # Check if the requested model exists
        if request.model not in model_paths:
            raise HTTPException(status_code=404, detail=f'Model {request.model} not found.')
        # Load the model based on the request
        model = joblib.load(f'models/{model_paths[request.model]}')

        # Prepare the input data for prediction
        df = pd.DataFrame([features.model_dump() for features in request.penguins])

        # Make predictions
        predictions = model.predict(df)

        # Prepare the response
        response = PredictResponse(
            model=request.model,
            species=predictions.tolist(),
            num_predictions=len(predictions)
        )

        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

