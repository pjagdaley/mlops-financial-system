from fastapi import FastAPI
import joblib
import numpy as np
from src.data_processing import preprocess_input
from app.schema import LoanRequest
from app.logger import setup_logger

app = FastAPI(title="MLOps Financial Prediction API")

# Load model once at startup
model = joblib.load("model/model.pkl")

logger = setup_logger()

@app.get("/")
def root():
    return {"message": "MLOps Financial API Running"}


@app.post("/predict")
def predict(request: LoanRequest):

    try:
        # Convert to dict
        data = request.dict()

        logger.info(f"Received request: {data}")

        # Preprocess
        df = preprocess_input(data)

        input_array = df.values

        prediction = model.predict(input_array)[0]

        result = "Approved" if prediction == 1 else "Rejected"

        logger.info(f"Prediction result: {result}")

        return {
            "prediction": int(prediction),
            "result": result
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": str(e)}