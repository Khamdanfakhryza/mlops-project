from fastapi import FastAPI, Request, HTTPException
import pandas as pd
import joblib
import time

from prometheus_client import Counter, Histogram, generate_latest, CollectorRegistry
from fastapi.responses import Response

app = FastAPI()

# =========================
# LOAD MODEL (LAZY LOAD)
# =========================
model = None

def get_model():
    global model
    if model is None:
        try:
            model = joblib.load("model.pkl")
        except Exception as e:
            raise RuntimeError(f"Model gagal diload: {e}")
    return model

# =========================
# ENCODING
# =========================
def encode_input(df):
    df["sex"] = df["sex"].map({"female": 0, "male": 1})
    df["smoker"] = df["smoker"].map({"no": 0, "yes": 1})
    df["region"] = df["region"].map({
        "southwest": 0,
        "southeast": 1,
        "northwest": 2,
        "northeast": 3
    })

    if df.isnull().any().any():
        raise HTTPException(status_code=400, detail="Input tidak valid")

    return df

# =========================
# PROMETHEUS METRICS (SAFE)
# =========================
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency"
)

ERROR_COUNT = Counter(
    "http_errors_total",
    "Total error count"
)

# =========================
# MIDDLEWARE
# =========================
@app.middleware("http")
async def track_metrics(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception:
        ERROR_COUNT.inc()
        status_code = 500
        raise

    duration = time.time() - start_time

    REQUEST_COUNT.labels(
        request.method,
        request.url.path,
        str(status_code)
    ).inc()

    REQUEST_LATENCY.observe(duration)

    return response

# =========================
# ENDPOINT
# =========================
@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: dict):
    required_fields = ["age", "sex", "bmi", "children", "smoker", "region"]

    for field in required_fields:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} wajib diisi")

    try:
        df = pd.DataFrame([data])

        df = encode_input(df)
        df["bmi_flag"] = df["bmi"].apply(lambda x: 1 if x > 30 else 0)

        model = get_model()
        result = model.predict(df)

        return {"prediction": float(result[0])}

    except Exception as e:
        ERROR_COUNT.inc()
        raise HTTPException(status_code=500, detail=str(e))

# =========================
# METRICS
# =========================
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")