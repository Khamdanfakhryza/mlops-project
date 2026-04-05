import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("preprocessing/scaler.pkl")

def predict(data):
    df = pd.DataFrame([data])

    df["sex"] = df["sex"].map({"female": 0, "male": 1})
    df["smoker"] = df["smoker"].map({"no": 0, "yes": 1})
    df["region"] = df["region"].map({
        "southwest": 0,
        "southeast": 1,
        "northwest": 2,
        "northeast": 3
    })

    df["bmi_flag"] = df["bmi"].apply(lambda x: 1 if x > 30 else 0)

    df_scaled = scaler.transform(df)

    result = model.predict(df_scaled)

    return float(result[0])