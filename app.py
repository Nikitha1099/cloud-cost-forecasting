from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model
model = joblib.load("models/cloud_cost_model.pkl")

# Define request model
class CostForecastRequest(BaseModel):
    cpu: float
    memory: float
    storage: float

# Define predict route
@app.post("/predict")
def predict_cost(data: CostForecastRequest):
    features = [[data.cpu, data.memory, data.storage]]  # ✅ Match 3 features
    prediction = model.predict(features)
    return {"predicted_cost": prediction[0]}
