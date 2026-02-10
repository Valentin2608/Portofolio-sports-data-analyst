from pathlib import Path
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss

# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "result" / "shots_features.csv"
OUTPUT_PATH = BASE_DIR / "result" / "shots_with_xg.csv"

# =========================
# Load data
# =========================
df = pd.read_csv(DATA_PATH)

# =========================
# Features & target
# =========================
X = df[["distance", "angle"]]
y = df["is_goal"]

# =========================
# Train / Test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# Model
# =========================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# =========================
# Evaluation
# =========================
y_pred_proba = model.predict_proba(X_test)[:, 1]

roc_auc = roc_auc_score(y_test, y_pred_proba)
logloss = log_loss(y_test, y_pred_proba)

print(f"ROC AUC : {roc_auc:.3f}")
print(f"Log Loss: {logloss:.3f}")

# =========================
# Coefficients (interprétation)
# =========================
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_[0]
})

print("\nCoefficients du modèle :")
print(coef_df)

# =========================
# xG prediction on full dataset
# =========================
df["xG"] = model.predict_proba(X)[:, 1]

# =========================
# Save
# =========================
df.to_csv(OUTPUT_PATH, index=False)

print(f"\nFichier avec xG sauvegardé : {OUTPUT_PATH}")
