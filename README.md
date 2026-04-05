Berikut versi README yang sudah disesuaikan dengan kondisi real project kamu (FastAPI + Prometheus + Grafana + MLflow + Codespaces URL) dan siap dipakai untuk submission / laporan.

⸻

🚀 MLOps Project: Medical Insurance Cost Prediction with Monitoring

Proyek ini merupakan implementasi end-to-end Machine Learning System (MLOps) yang mencakup:
	•	Data preprocessing
	•	Model training & tracking (MLflow)
	•	Model serving (FastAPI)
	•	Monitoring (Prometheus + Grafana)
	•	Deployment berbasis GitHub Codespaces

🌐 Live API (Swagger UI):
👉 https://sturdy-fiesta-q795774rw6jr29v47-8000.app.github.dev/docs

⸻

📂 Struktur Repository

mlops-project/
├── inference.py                 # FastAPI serving + metrics Prometheus
├── model.pkl                   # Model hasil training
├── prometheus.yml              # Config Prometheus
├── prometheus_exporter.py      # (opsional lama)
├── requirements.txt
├── mlflow.db
├── .github/workflows/
│   └── mlops.yml               # CI/CD pipeline
└── README.md


⸻

📊 Dataset

Dataset: Medical Insurance Cost Dataset (Kaggle)

Fitur:
	•	age
	•	sex
	•	bmi
	•	children
	•	smoker
	•	region

Target:
	•	charges (biaya asuransi)

⸻

⚙️ Arsitektur Sistem

User → FastAPI → Model (.pkl)
                ↓
           Prometheus (/metrics)
                ↓
             Grafana

Tambahan:
	•	MLflow → tracking eksperimen

⸻

🚀 CARA MENJALANKAN SISTEM (FULL STEP)

1. Jalankan FastAPI (Serving Model)

uvicorn inference:app --host 0.0.0.0 --port 8000

Akses:
	•	Swagger UI:
👉 https://sturdy-fiesta-q795774rw6jr29v47-8000.app.github.dev/docs
	•	Metrics:
👉 https://sturdy-fiesta-q795774rw6jr29v47-8000.app.github.dev/metrics

⸻

2. Jalankan MLflow (Tracking)

mlflow ui --host 0.0.0.0 --port 5000

Akses:
👉 https://sturdy-fiesta-q795774rw6jr29v47-5000.app.github.dev

⸻

3. Jalankan Prometheus

Konfigurasi (prometheus.yml)

global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'ml-api'
    metrics_path: /metrics
    scheme: https
    static_configs:
      - targets: ['sturdy-fiesta-q795774rw6jr29v47-8000.app.github.dev']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['172.17.0.1:8080']

Jalankan:

docker run -p 9090:9090 \
-v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus

Akses:
👉 https://sturdy-fiesta-q795774rw6jr29v47-9090.app.github.dev

Cek:
👉 /targets → harus UP

⸻

4. Jalankan Grafana

docker run -d -p 3000:3000 grafana/grafana

Akses:
👉 https://sturdy-fiesta-q795774rw6jr29v47-3000.app.github.dev

Login:

user: admin
pass: admin


⸻

🔗 CONNECT GRAFANA KE PROMETHEUS

Masuk:
	•	Connections → Data Sources → Add Prometheus

Isi:

URL: http://172.17.0.1:9090

Klik:
👉 Save & Test (harus SUCCESS)

⸻

📊 QUERY GRAFANA (SIAP PAKAI)

1. Request Rate (Throughput)

rate(http_requests_total[1m])

2. Request /predict saja

rate(http_requests_total{endpoint="/predict"}[1m])

3. Total Request

sum(http_requests_total)

4. Error Rate

rate(http_errors_total[1m])

5. Latency (Average)

rate(http_request_duration_seconds_sum[1m])
/
rate(http_request_duration_seconds_count[1m])

6. Memory Usage

process_resident_memory_bytes

7. CPU Usage

process_cpu_seconds_total


⸻

🧪 TEST LOAD (SIMULASI REQUEST)

Jalankan:

for i in {1..50};
do
curl -X POST https://sturdy-fiesta-q795774rw6jr29v47-8000.app.github.dev/predict \
-H "Content-Type: application/json" \
-d '{"age":30,"sex":"male","bmi":28.5,"children":2,"smoker":"no","region":"northwest"}'
done


⸻

📈 HASIL MONITORING

Berdasarkan metrics:
	•	Total request /predict: 463+
	•	Total request keseluruhan: 863
	•	Error: 1
	•	Latency total: ~9.43 detik
	•	Avg latency ≈ 0.01 detik
	•	Memory: ~218 MB
	•	CPU time: 14.54 detik

⸻

🧠 METRICS YANG DIGUNAKAN

Custom Metrics
	•	http_requests_total
	•	http_request_duration_seconds
	•	http_errors_total

Default Metrics (Prometheus Python)
	•	CPU usage
	•	Memory usage
	•	GC statistics

⸻

🏆 FITUR UTAMA

✅ FastAPI serving
✅ Prometheus metrics integration
✅ Grafana dashboard
✅ MLflow experiment tracking
✅ Docker-based monitoring
✅ Real-time visualization

⸻

📌 KESIMPULAN

Proyek ini berhasil membangun sistem MLOps lengkap:
	1.	Model dapat di-serve via API
	2.	Semua request termonitor
	3.	Performa (latency, throughput) terukur
	4.	Resource (CPU, RAM) terpantau
	5.	Visualisasi real-time via Grafana

⸻

✨ NEXT IMPROVEMENT
	•	Alerting Grafana (CPU tinggi, error spike)
	•	Deploy ke Kubernetes
	•	Auto-scaling API
	•	Logging ke ELK Stack

⸻