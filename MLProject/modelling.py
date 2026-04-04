import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("insurance.csv")

# ===============================
# ENCODING
# ===============================
encoder = LabelEncoder()
for col in ["sex", "smoker", "region"]:
    df[col] = encoder.fit_transform(df[col])

# ===============================
# FEATURE ENGINEERING
# ===============================
df["bmi_flag"] = df["bmi"].apply(lambda x: 1 if x > 30 else 0)

# ===============================
# SPLIT DATA
# ===============================
X = df.drop("charges", axis=1)
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# MODEL
# ===============================
model = RandomForestRegressor(
    n_estimators=120,
    max_depth=6,
    random_state=42
)

# ===============================
# TRAINING
# ===============================
model.fit(X_train, y_train)

# ===============================
# EVALUATION
# ===============================
pred = model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

# ===============================
# MLFLOW LOGGING (NO start_run, NO tracking_uri)
# ===============================
mlflow.log_param("n_estimators", 120)
mlflow.log_param("max_depth", 6)

mlflow.log_metric("MAE", float(mae))
mlflow.log_metric("R2", float(r2))

mlflow.sklearn.log_model(model, "model")

# ===============================
# OUTPUT
# ===============================
print("Training selesai")
print("MAE:", mae)
print("R2:", r2)