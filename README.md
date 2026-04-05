Berikut README yang sudah disesuaikan dengan kondisi real project kamu (Docker + FastAPI + Prometheus + Grafana + endpoint aktif) 👇

⸻

🚀 MLOps Project: Medical Insurance Prediction + Monitoring

Proyek ini merupakan implementasi end-to-end Machine Learning System (MLOps) yang mencakup:
	•	Model training (MLflow)
	•	Model serving (FastAPI)
	•	Monitoring (Prometheus + Grafana)
	•	Containerization (Docker)

⸻

📌 Arsitektur Sistem

Client → FastAPI (8000) → Model Prediction
                     ↓
                 /metrics
                     ↓
             Prometheus (9090)
                     ↓
               Grafana (3000)


⸻

📂 Struktur Project

mlops-project/
├── inference.py              # FastAPI API + metrics
├── model.pkl                # Model hasil training
├── prometheus.yml           # Config Prometheus
├── docker-compose.yml       # Orkestrasi container
├── Dockerfile               # Build API container
├── requirements.txt
├── mlruns/                  # MLflow tracking
├── README.md


⸻

⚙️ FITUR UTAMA

✅ 1. Model Prediction API
	•	Framework: FastAPI
	•	Endpoint:
	•	/predict
	•	/metrics

⸻

✅ 2. Monitoring (Prometheus)
	•	Track:
	•	Request count
	•	Latency
	•	Error rate

⸻

✅ 3. Visualization (Grafana)
	•	Dashboard:
	•	Throughput
	•	Latency
	•	Error monitoring

⸻

✅ 4. Containerized System
	•	Semua service jalan via Docker:
	•	ml-api → 8000
	•	prometheus → 9090
	•	grafana → 3000
	•	cadvisor → 8080

⸻

▶️ CARA MENJALANKAN PROJECT

1. Build & Run Semua Service

docker-compose up -d --build


⸻

2. Cek Container

docker ps

Harus muncul:
	•	ml-api
	•	prometheus
	•	grafana
	•	cadvisor

⸻

🌐 AKSES SERVICE

🔹 FastAPI (API + Docs)

http://localhost:8000/docs

👉 (Codespaces)

https://<your-url>-8000.app.github.dev/docs


⸻

🔹 Prometheus

http://localhost:9090

👉 Codespaces:

https://<your-url>-9090.app.github.dev


⸻

🔹 Grafana

http://localhost:3000

Login:

user: admin
pass: admin


⸻

🔗 SETTING GRAFANA (WAJIB)

Tambahkan Data Source

Isi:

Name: prometheus
URL: http://prometheus:9090
Access: Server

Klik:

Save & Test


⸻

📊 QUERY GRAFANA

🔹 Total Request

http_requests_total


⸻

🔹 Request Rate (Predict)

rate(http_requests_total{endpoint="/predict"}[1m])


⸻

🔹 Latency

histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[1m]))


⸻

🔹 Error Rate

http_errors_total


⸻

📡 CONTOH REQUEST API

Endpoint:

POST /predict

URL:

http://localhost:8000/predict

Body:

{
  "age": 30,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "northwest"
}


⸻

🧠 METRICS YANG TERSEDIA

Metric	Deskripsi
http_requests_total	Total request
http_request_duration_seconds	Latency
http_errors_total	Error count


⸻

🐳 DOCKER COMMANDS

Restart Grafana

docker restart <container_id>


⸻

Jalankan Grafana Manual

docker run -d -p 3000:3000 grafana/grafana


⸻

Stop Semua

docker-compose down


⸻

Rebuild

docker-compose up -d --build


⸻

🔧 GIT WORKFLOW

git status
git add .
git commit -m "feat: integrate Prometheus monitoring with FastAPI deployment (metrics endpoint)"
git pull origin main --rebase
git push origin main


⸻

⚠️ TROUBLESHOOTING

❌ Grafana tidak connect Prometheus

✔ Gunakan:

http://prometheus:9090

❌ Jangan pakai:
	•	localhost
	•	IP 172.x.x.x

⸻

❌ Port sudah dipakai

lsof -i :8000
kill -9 <PID>


⸻

❌ Container ml-api mati

docker logs ml-api

Biasanya:

ModuleNotFoundError: prometheus_client

👉 Fix:

pip install prometheus_client


⸻

❌ Metrics tidak terbaca

Pastikan:

http://localhost:8000/metrics

menampilkan:

# HELP http_requests_total ...


⸻

🎯 HASIL AKHIR

✅ API berjalan
✅ Model inference aktif
✅ Metrics masuk Prometheus
✅ Dashboard Grafana aktif

⸻

✨ PENUTUP

Proyek ini menunjukkan implementasi lengkap:
	•	Machine Learning → Deployment → Monitoring → Visualization

Cocok untuk:
	•	MLOps pipeline
	•	Production-ready system
	•	Monitoring observability

⸻