# Import necessary libraries
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize FastAPI
app = FastAPI()

# Define request body schema
class SepssisFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int  

# Load pre-trained models and encoders
forest_pipeline = joblib.load("./models/rf_classifier_pipeline.joblib")
decision_tree_pipeline = joblib.load("./models/tree_classifier_pipeline.joblib")
logistic_pipeline = joblib.load("./models/logistic_classifier_pipeline.joblib")
encoder = joblib.load("./models/label_encoder.joblib")

# Define endpoint for home page
@app.get('/')
def home():   
    return {
        "title": "Welcome to the Sepsis Prediction API!",
        "description": "This API provides endpoints for predicting the likelihood of sepsis based on patient data.",
        "endpoints": {
            "/predict_random_forest": "Predict sepsis using the Random Forest model.",
            "/predict_decision_tree": "Predict sepsis using the Decision Tree model.",
            "/predict_logistic": "Predict sepsis using the Logistic Regression model."
        },
        "usage": {
            "method": "POST",
            "content_type": "application/json",
            "data_structure": {
                "PRG": "Positive Real number",
                "PL": "Positive Real number",
                "PR": "Positive Real number",
                "SK": "Positive Real number",
                "TS": "Positive Real number",
                "M11": "Real number",
                "BD2": "Real number",
                "Age": "Integer",
                "Insurance": "Integer"
            },
            "example_data": {
                "PRG": 120,
                "PL": 80,
                "PR": 100,
                "SK": 90,
                "TS": 70,
                "M11": 0.15,
                "BD2": 0.25,
                "Age": 45,
                "Insurance": 1
            }
        }
    }

# Define endpoint for predicting with Random Forest model
@app.post("/predict_Random_Forest_Model")
def predict_Random_Forest(data: SepssisFeatures):
    
    df = pd.DataFrame([data.model_dump()])  # Convert input data to DataFrame

    prediction = forest_pipeline.predict(df) # Make prediction using the Random Forest model

    prediction = int(prediction[0]) # Convert the prediction to an integer, selecting the first element of the prediction array

    prediction = encoder.inverse_transform([prediction])[0] # Inverse transform the prediction using the encoder

    probabilities = forest_pipeline.predict_proba(df)  # predict probabilities for each class

    probabilities = probabilities.tolist() # convert the probability result to a list

    return {'predictions': prediction, 'probabilities': probabilities}

# Define endpoint for predicting with Decision Tree model
@app.post("/predict_Decision_Tree_Model")
def predict_Decision_Tree(data: SepssisFeatures):
    
    df = pd.DataFrame([data.model_dump()])  # Convert input data to DataFrame

    prediction = decision_tree_pipeline.predict(df)  # Make prediction using the Decision Tree model

    prediction = int(prediction[0]) # Convert the prediction to an integer, selecting the first element of the prediction array

    prediction = encoder.inverse_transform([prediction])[0] # Inverse transform the prediction using the encoder

    probabilities = decision_tree_pipeline.predict_proba(df) # predict probabilities for each class

    probabilities = probabilities.tolist() # convert the probability result to a list

    return {'predictions': prediction, 'probabilities': probabilities}

# Define endpoint for predicting with Logistic Regression model
@app.post("/predict_Logistic_Model")
def predict_Logistic(data: SepssisFeatures):
    
    df = pd.DataFrame([data.model_dump()]) # Convert input data to DataFrame

    prediction = logistic_pipeline.predict(df)  # Make prediction using the Logistic regression model

    prediction = int(prediction[0])  # Convert the prediction to an integer, selecting the first element of the prediction array

    prediction = encoder.inverse_transform([prediction])[0]  # Inverse transform the prediction using the encoder

    probabilities = logistic_pipeline.predict_proba(df) # predict probabilities for each class

    probabilities = probabilities.tolist() # convert the probability result to a list

    return {'predictions': prediction, 'probabilities': probabilities}

# Run the FastAPI app
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)