from pydantic import BaseModel, Field
from typing import Literal, List

class PenguinFeatures(BaseModel):
    island: Literal['Biscoe', 'Dream', 'Torgersen']
    bill_length_mm: float = Field(..., ge=0)
    bill_depth_mm: float = Field(..., ge=0)
    flipper_length_mm: float = Field(..., ge=0)  # Flipper length is typically measured in millimeters.
    body_mass_g: float = Field(..., ge=0)        # Body mass is typically measured in grams.
    sex: Literal['male', 'female']

class PredictRequest(BaseModel):
    model: str
    penguins: List[PenguinFeatures]

class PredictResponse(BaseModel):
    model: str
    species: List[str]
    num_predictions: int