from inference import predict

data = {
    "age": 30,
    "sex": "male",
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
}

print("Prediction:", predict(data))
