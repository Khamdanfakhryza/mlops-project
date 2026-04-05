import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# =========================
# BASE PATH (WAJIB)
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "dataset", "insurance.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "preprocessing")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(DATA_PATH)

# =========================
# ENCODING
# =========================
df['sex'] = df['sex'].map({'female': 0, 'male': 1})
df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})
df['region'] = df['region'].map({
    'southwest': 0,
    'southeast': 1,
    'northwest': 2,
    'northeast': 3
})

# =========================
# FEATURE ENGINEERING
# =========================
df['bmi_flag'] = df['bmi'].apply(lambda x: 1 if x > 30 else 0)

# =========================
# SPLIT DATA
# =========================
X = df.drop("charges", axis=1)
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# SCALING
# =========================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================
# SAVE ARTIFACT (FIXED)
# =========================
joblib.dump(scaler, os.path.join(OUTPUT_DIR, "scaler.pkl"))

pd.DataFrame(X_train_scaled, columns=X.columns).to_csv(
    os.path.join(OUTPUT_DIR, "X_train.csv"), index=False
)

pd.DataFrame(X_test_scaled, columns=X.columns).to_csv(
    os.path.join(OUTPUT_DIR, "X_test.csv"), index=False
)

y_train.to_csv(os.path.join(OUTPUT_DIR, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(OUTPUT_DIR, "y_test.csv"), index=False)

print("✅ Preprocessing selesai & tersimpan dengan benar!")