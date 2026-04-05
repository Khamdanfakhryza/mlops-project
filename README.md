# 🚀 MLOps Project: Medical Insurance Prediction + Monitoring

Proyek ini merupakan implementasi **end-to-end Machine Learning System (MLOps)** yang mencakup:

- Model training (MLflow)
- Model serving (FastAPI)
- Monitoring (Prometheus + Grafana)
- Containerization (Docker)

---

## 📌 Arsitektur Sistem

```
Client → FastAPI (8000) → Model Prediction
                     ↓
                 /metrics
                     ↓
             Prometheus (9090)
                     ↓
               Grafana (3000)
```

---

## 📂 Struktur Project

```
mlops-project/
├── inference.py
├── model.pkl
├── prometheus.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── mlruns/
├── README.md
```

---

## ⚙️ FITUR UTAMA

### ✅ Model Prediction API
- FastAPI
- Endpoint: /predict, /metrics

### ✅ Monitoring
- Prometheus (request, latency, error)

### ✅ Visualization
- Grafana dashboard

### ✅ Containerized
- ml-api (8000)
- prometheus (9090)
- grafana (3000)
- cadvisor (8080)

---

## ▶️ CARA MENJALANKAN

```bash
docker-compose up -d --build
```

Cek:
```bash
docker ps
```

---

## 🌐 AKSES

FastAPI:
http://localhost:8000/docs

Prometheus:
http://localhost:9090

Grafana:
http://localhost:3000
(user: admin / pass: admin)

---

## 🔗 GRAFANA SETUP

- URL: http://prometheus:9090
- Access: Server

---

## 📊 QUERY

```
http_requests_total
rate(http_requests_total{endpoint="/predict"}[1m])
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[1m]))
http_errors_total
```

---

## 📡 CONTOH REQUEST

```
POST /predict
```

Body:
```json
{
  "age": 30,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "northwest"
}
```

---

## 🐳 DOCKER

Stop:
```bash
docker-compose down
```

Rebuild:
```bash
docker-compose up -d --build
```

---

## 🔧 GIT

```bash
git status
git add .
git commit -m "feat: integrate Prometheus monitoring with FastAPI deployment (metrics endpoint)"
git pull origin main --rebase
git push origin main
```

---

## 🎯 HASIL

- API jalan
- Monitoring aktif
- Dashboard Grafana aktif
