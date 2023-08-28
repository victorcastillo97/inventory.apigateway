from fastapi import APIRouter
from core.config import INVENTORY_SERVICE_URL
import requests

router = APIRouter()

@router.get("/{customer_id}")
def read_customer(customer_id: int):
    response = requests.get(f"{INVENTORY_SERVICE_URL}/customers/{customer_id}")
    return response.json()

@router.post("/")
def create_customer(data: dict):
    response = requests.post(f"{INVENTORY_SERVICE_URL}/customers/", json=data)
    return response.json()