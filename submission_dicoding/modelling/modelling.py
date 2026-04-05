import os
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =========================
# PATH SETUP
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "preprocessing")

# =========================
# LOAD DATA
# =========================
X_train = pd.read_csv(os.path.join(DATA_DIR, "X_train.csv"))
X_test = pd.read_csv(os.path.join(DATA_DIR, "X_test.csv"))
y_train = pd.read_csv(os.path.join(DATA_DIR, "y_train.csv")).values.ravel()
y_test = pd.read_csv(os.path.join(DATA_DIR, "y_test.csv")).values.ravel()

# =========================
# MLFLOW SETUP
# =========================
mlflow.set_experiment("insurance-prediction")

# =========================
# TRAINING
# =========================
with mlflow.start_run():

    model = LinearRegression()
    model.fit(X_train, y_train)

    # =========================
    # PREDICT
    # =========================
    y_pred = model.predict(X_test)

    # =========================
    # METRICS (FIXED)
    # =========================
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"RMSE: {rmse}")
    print(f"R2 Score: {r2}")

    # =========================
    # LOGGING
    # =========================
    mlflow.log_param("model", "LinearRegression")
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)

    mlflow.sklearn.log_model(model, "model")

    # =========================
    # SAVE MODEL
    # =========================
    import joblib
    joblib.dump(model, os.path.join(BASE_DIR, "model.pkl"))

print("✅ Training selesai & model tersimpan!")