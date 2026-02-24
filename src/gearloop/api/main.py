# src/gearloop_agent/api/main.py

from fastapi import FastAPI

# FastAPI this is the main entry point for our API server.
app = FastAPI(title="GearLoop Agent API")


@app.get("/health")
def health_check():
    """
    Health check endpoint:
    - Purpose: Allows monitoring systems to quickly determine if the service is running correctly
    - Returns a simple dictionary {"status": "ok"}
    """
    return {"status": "ok"}


@app.get("/recommend")
def recommend_stub():
    """
    Recommendation endpoint (stub version):
    - Will be handled by our Agent orchestrator later
    """
    demo_item = {
        "product_id": "demo_ski_001",
        "name": "Demo All-Mountain Ski 172",
        "brand": "GearLoop",
        "price": 599.99,
        "currency": "CAD",
        "reason": "Demo response",
    }
    return {"items": [demo_item]}