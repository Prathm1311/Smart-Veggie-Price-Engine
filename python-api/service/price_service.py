import joblib
import pandas as pd
from pathlib import Path

class PricePredictionService:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent

        self.model = joblib.load(base_dir / "ml_model" / "vegetable_price_model.pkl")
        self.veg_encoder = joblib.load(base_dir / "ml_model" / "veg_encoder.pkl")
        self.season_encoder = joblib.load(base_dir / "ml_model" / "season_encoder.pkl")
        self.demand_encoder = joblib.load(base_dir / "ml_model" / "demand_encoder.pkl")
        print("✅ PricePredictionService initialized")
    def predict_final_price(
        self,
        vegetable: str,
        season: str,
        demand: str,
        base_price: float
    ) -> float:

        vegetable = vegetable.capitalize()
        season = season.capitalize()
        demand = demand.capitalize()

        veg = self.veg_encoder.transform([vegetable])[0]
        sea = self.season_encoder.transform([season])[0]
        dem = self.demand_encoder.transform([demand])[0]

        X = pd.DataFrame(
            [[veg, sea, dem]],
            columns=["vegetable", "season", "demand_level"]
        )

        price_change_percent = self.model.predict(X)[0]

        final_price = base_price + (base_price * price_change_percent / 100)
      
        print("\n💰 FINAL PRICE")
        print("Final Price:", final_price)
        print("Type:", type(final_price))
        return float(round(final_price, 2))
