# ...existing code...
# import joblib
# import json

# with open("models/models.json") as f:
#     model_paths = json.load(f)

# models = {name: joblib.load(path) for name, path in model_paths.items()}
# ...existing code...

from fastapi import FastAPI, HTTPException
from data_models import PredictRequest, PredictResponse
import joblib

app = FastAPI(title="Penguin Species Prediction API", version="1.0", description="API for predicting penguin species using trained models.")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Penguin Species Prediction API, ACTUALIZADO!"}

# @app.post("/predict", response_model=PredictResponse)
# def predict_species(request: PredictRequest) -> PredictResponse:
