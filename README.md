# Project - Car Price Prediction API

This project is a machine learning application that predicts the price of cars based on certain features such as engine volume, mileage, and other vehicle specifications. The model is built using **Random Forests**, and an **API** is created using **FastAPI** to interact with the model and make predictions.

## Features

- Predict car prices based on the following features:
  - Levy
  - Production Year
  - Engine Volume
  - Mileage
  - Cylinders
  - Doors
  - Airbags

 ## Running the API

After setting up the environment, run the FastAPI application.

### Example Request:

You can use tools like Postman or cURL to make a POST request to the following endpoint:

-   **POST** `http://127.0.0.1:8000/predict/`

#### Example body for the request:

json

Copy

`{
  "Levy": 3000,
  "Prod. year": 2015,
  "Engine volume": 2.5,
  "Mileage": 75000,
  "Cylinders": 4,
  "Doors": 4,
  "Airbags": 6
} `

The response will give you the predicted price for the car based on the input features.

Model Download Instructions
---------------------------

The trained model (`best_model.pkl`) used for car price prediction is stored on Google Drive at the below link:

Link: https://drive.google.com/file/d/1OwRWb5OQAnHAcH_A16ZEkpZpnSTviYN0/view?usp=sharing


