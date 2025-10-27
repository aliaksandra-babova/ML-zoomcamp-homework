import pickle

import uvicorn
from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI(title="conv-prediction")

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

@app.post("/predict")

def predict_convertion(lead: Dict[str, Any]):
    result = pipeline.predict_proba(lead)[0, 1]
    return float(result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)