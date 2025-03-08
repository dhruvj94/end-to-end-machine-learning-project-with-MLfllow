import joblib
from pathlib import Path
import pandas as pd
import numpy as np

STAGE_NAME = "Prediction stage"

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))


    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction