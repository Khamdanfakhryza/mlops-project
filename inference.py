from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

# Load model
model = joblib.load("model.pkl")

def encode_input(df):
    df["sex"] = df["sex"].map({"female": 0, "male": 1})
    df["smoker"] = df["smoker"].map({"no": 0, "yes": 1})
    df["region"] = df["region"].map({
        "southwest": 0,
        "southeast": 1,
        "northwest": 2,
        "northeast": 3
    })
    return df

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    # Encoding FIX
    df = encode_input(df)

    # Feature engineering
    df["bmi_flag"] = df["bmi"].apply(lambda x: 1 if x > 30 else 0)

    result = model.predict(df)

    return {"prediction": float(result[0])}