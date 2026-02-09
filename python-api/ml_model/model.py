import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# project root
BASE_DIR = Path(__file__).resolve().parent.parent

# load dataset
data = pd.read_csv(
    BASE_DIR / "dataset" / "vegetable_price_training_data.csv"
)

# encoders
veg_encoder = LabelEncoder()
season_encoder = LabelEncoder()
demand_encoder = LabelEncoder()

data["vegetable"] = veg_encoder.fit_transform(data["vegetable"])
data["season"] = season_encoder.fit_transform(data["season"])
data["demand_level"] = demand_encoder.fit_transform(data["demand_level"])

X = data[["vegetable", "season", "demand_level"]]
y = data["price_change_percent"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)

print("✅ Model trained")
print("📊 R2 score:", r2_score(y_test, model.predict(X_test)))

# save outputs
joblib.dump(model, BASE_DIR / "ml_model" / "vegetable_price_model.pkl")
joblib.dump(veg_encoder, BASE_DIR / "ml_model" / "veg_encoder.pkl")
joblib.dump(season_encoder, BASE_DIR / "ml_model" / "season_encoder.pkl")
joblib.dump(demand_encoder, BASE_DIR / "ml_model" / "demand_encoder.pkl")

print("💾 Model & encoders saved in ml_model/")
