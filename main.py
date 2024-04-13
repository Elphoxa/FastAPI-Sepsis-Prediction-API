from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

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

forest_pipeline = joblib.load("./models/rf_classifier_pipeline.joblib")
decision_tree_pipeline = joblib.load("./models/tree_classifier_pipeline.joblib")
logistic_pipeline = joblib.load("./models/logistic_classifier_pipeline.joblib")
encoder = joblib.load("./models/label_encoder.joblib")

@app.get('/')
def home():
    return {"Hello World"}

# Info route
@app.get('/info')
def appinfo():
    return {
        "title": "Welcome to the Sepsis Prediction API!",
    }

@app.post("/predict_Random_Forest_Model")
def predict_Random_Forest(data: SepssisFeatures):
    df = pd.DataFrame([data.model_dump()])

    prediction = forest_pipeline.predict(df)

    prediction = int(prediction[0])

    prediction = encoder.inverse_transform([prediction])[0]

    probabilities = forest_pipeline.predict_proba(df)

    probabilities = probabilities.tolist()

    return {'predictions': prediction, 'probabilities': probabilities}

@app.post("/predict_Decision_Tree_Model")
def predict_Decision_Tree(data: SepssisFeatures):
    df = pd.DataFrame([data.model_dump()])

    prediction = decision_tree_pipeline.predict(df)

    prediction = int(prediction[0])

    prediction = encoder.inverse_transform([prediction])[0]

    probabilities = decision_tree_pipeline.predict_proba(df)

    probabilities = probabilities.tolist()

    return {'predictions': prediction, 'probabilities': probabilities}

@app.post("/predict_Logistic_Model")
def predict_Logistic(data: SepssisFeatures):
    df = pd.DataFrame([data.model_dump()])

    prediction = logistic_pipeline.predict(df)

    prediction = int(prediction[0])

    prediction = encoder.inverse_transform([prediction])[0]

    probabilities = logistic_pipeline.predict_proba(df)

    probabilities = probabilities.tolist()

    return {'predictions': prediction, 'probabilities': probabilities}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
