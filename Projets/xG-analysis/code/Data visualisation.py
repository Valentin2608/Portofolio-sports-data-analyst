from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "result" / "shots_with_xg.csv"
FIG_DIR = BASE_DIR / "result" / "figures"
FIG_DIR.mkdir(exist_ok=True)

# =========================
# Load data
# =========================
df = pd.read_csv(DATA_PATH)

# =========================
# 1. xG vs Distance
# =========================
plt.figure()
plt.scatter(df["distance"], df["xG"], alpha=0.3)
plt.xlabel("Shot distance (meters)")
plt.ylabel("Expected Goals (xG)")
plt.title("xG vs Shot Distance")
plt.tight_layout()
plt.savefig(FIG_DIR / "xg_vs_distance.png")
plt.close()

# =========================
# 2. Distribution des xG
# =========================
plt.figure()
plt.hist(df["xG"], bins=30)
plt.xlabel("Expected Goals (xG)")
plt.ylabel("Number of shots")
plt.title("Distribution of Expected Goals")
plt.tight_layout()
plt.savefig(FIG_DIR / "xg_distribution.png")
plt.close()

# =========================
# 3. Goals vs xG
# =========================
plt.figure()
plt.scatter(df["xG"], df["is_goal"], alpha=0.3)
plt.xlabel("Expected Goals (xG)")
plt.ylabel("Goal (1 = goal)")
plt.title("Goals vs Expected Goals")
plt.tight_layout()
plt.savefig(FIG_DIR / "goals_vs_xg.png")
plt.close()

print("Visualisations xG générées dans result/figures/")
