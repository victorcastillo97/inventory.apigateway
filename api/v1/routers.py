from fastapi import APIRouter
from .endpoints import products, customers, orders

router = APIRouter()

router.include_router(products.router, prefix="/products", tags=["products"])
router.include_router(customers.router, prefix="/customers", tags=["customers"])
router.include_router(orders.router, prefix="/orders", tags=["orders"])