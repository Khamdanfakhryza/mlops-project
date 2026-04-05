from fastapi import FastAPI, Request
import pandas as pd
import joblib
import time

from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response

app = FastAPI()

# =========================
# LOAD MODEL
# =========================
model = joblib.load("model.pkl")

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
    return df

# =========================
# PROMETHEUS METRICS
# =========================
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint"]
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
    except Exception:
        ERROR_COUNT.inc()
        raise

    duration = time.time() - start_time

    REQUEST_COUNT.labels(request.method, request.url.path).inc()
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
    df = pd.DataFrame([data])

    df = encode_input(df)
    df["bmi_flag"] = df["bmi"].apply(lambda x: 1 if x > 30 else 0)

    result = model.predict(df)

    return {"prediction": float(result[0])}

# =========================
# METRICS (WAJIB 1x SAJA)
# =========================
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")