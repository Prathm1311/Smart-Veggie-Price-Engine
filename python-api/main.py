from fastapi import FastAPI
from controller.price_controller import router as price_router

app = FastAPI(
    title="Vegetable Price Prediction API",
    version="1.0"
)

app.include_router(price_router)

@app.get("/")
def health():
    return {"status": "Price Prediction Service Running 🚀"}
