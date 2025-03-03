from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os
import gdown

# Get the Google Drive file ID from the environment variable
file_id = os.getenv('GOOGLE_DRIVE_FILE_ID')

# Construct the Google Drive download link
download_link = f"https://drive.google.com/uc?id={file_id}"

# Download the model file from Google Drive
gdown.download(download_link, 'best_model.pkl', quiet=False)

# Load the trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Create an instance of the FastAPI app
app = FastAPI()

# Define the input structure using Pydantic (with the reduced set of features)
class CarFeatures(BaseModel):
    Levy: float
    Prod_year: int
    Engine_volume: float
    Mileage: float
    Cylinders: float
    Doors: int
    Airbags: int

# Define the prediction endpoint
@app.post("/predict/")
def predict_price(car_features: CarFeatures):
    # Create an array with the selected features
    input_data = np.array([[
        car_features.Levy,
        car_features.Prod_year,
        car_features.Engine_volume,
        car_features.Mileage,
        car_features.Cylinders,
        car_features.Doors,
        car_features.Airbags
    ]])

    # Make prediction using the trained model
    predicted_price = model.predict(input_data)

    # Return the predicted price
    return {"predicted_price": predicted_price[0]}
