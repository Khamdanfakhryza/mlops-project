from fastapi import FastAPI
from prometheus_client import Counter, Gauge, generate_latest
from fastapi.responses import Response

app = FastAPI()

# Counter metrics
REQUEST_COUNT = Counter('request_count', 'Total API Requests')
PREDICT_COUNT = Counter('predict_count', 'Total Prediction Requests')

# Gauge metric (tambahan)
CPU_USAGE = Gauge('cpu_usage', 'CPU usage simulation')

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    CPU_USAGE.set(50)  # update nilai
    return {"status": "running"}

@app.post("/predict")
def predict():
    REQUEST_COUNT.inc()
    PREDICT_COUNT.inc()
    CPU_USAGE.set(60)  # simulasi naik
    return {"message": "prediction simulated"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")