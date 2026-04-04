# mlops-project
End-to-end machine learning system for insurance cost prediction using MLflow, FastAPI, and monitoring tools.

## 🚀 Live API
- Base URL: https://mlops-api-k2mu.onrender.com
- Docs: https://mlops-api-k2mu.onrender.com/docs

## Example Request
POST /predict
{
  "age": 30,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "northwest"
}
