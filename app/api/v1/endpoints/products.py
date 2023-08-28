from fastapi import APIRouter
from core.config import INVENTORY_SERVICE_URL
import requests

router = APIRouter()

@router.get("/")
def read_products():
    response = requests.get(f"{INVENTORY_SERVICE_URL}/products/")
    return response.json()

@router.put("/")
def update_product(data: dict):
    response = requests.put(f"{INVENTORY_SERVICE_URL}/products/", json=data)
    return response.json()

@router.post("/")
def create_product(data: dict):
    response = requests.post(f"{INVENTORY_SERVICE_URL}/products/", json=data)
    return response.json()

@router.get("/{product_id}")
def read_product(product_id: int):
    response = requests.get(f"{INVENTORY_SERVICE_URL}/products/{product_id}")
    return response.json()

@router.delete("/{product_id}")
def delete_product(product_id: int):
    response = requests.delete(f"{INVENTORY_SERVICE_URL}/products/{product_id}")
    return response.json()