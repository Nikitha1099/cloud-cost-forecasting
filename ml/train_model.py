# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load your dataset (replace this with your actual path)
df = pd.read_csv("data/cloud_cost_data.csv")  # Make sure the CSV contains cpu, memory, storage, cost columns

# Define input features and target
X = df[["cpu", "memory", "storage"]]  # 3 features
y = df["cost"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/cloud_cost_model.pkl")

print("Model trained and saved to models/cloud_cost_model.pkl")
