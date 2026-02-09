from fastapi import APIRouter
from pydantic import BaseModel
from service.price_service import PricePredictionService

router = APIRouter()
service = PricePredictionService()

class PriceRequest(BaseModel):
    vegetable: str
    season: str
    demand: str
    base_price: float

@router.post("/predict")
def predict_price(req: PriceRequest):
    final_price = service.predict_final_price(
        req.vegetable,
        req.season,
        req.demand,
        req.base_price,

    )
    return {
        "predicted_final_price": float(final_price)
    }


