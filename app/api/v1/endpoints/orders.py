from fastapi import APIRouter
from core.config import INVENTORY_SERVICE_URL
import requests

router = APIRouter()

@router.get("/")
def read_orders():
    response = requests.get(f"{INVENTORY_SERVICE_URL}/orders/")
    return response.json()

@router.post("/")
def create_complete_order(data: dict):
    response = requests.post(f"{INVENTORY_SERVICE_URL}/orders/complete", json=data)
    return response.json()