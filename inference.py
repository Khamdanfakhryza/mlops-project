from fastapi import FastAPI
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

# Load model
model = joblib.load("model.pkl")

# Encoder (harus sama seperti training)
encoder = LabelEncoder()

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    # Encoding (WAJIB biar tidak error)
    for col in ["sex", "smoker", "region"]:
        df[col] = encoder.fit_transform(df[col])

    # Feature tambahan (harus sama dengan training)
    df["bmi_flag"] = df["bmi"].apply(lambda x: 1 if x > 30 else 0)

    result = model.predict(df)

    return {"prediction": float(result[0])}