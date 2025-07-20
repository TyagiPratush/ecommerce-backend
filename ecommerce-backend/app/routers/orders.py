from fastapi import APIRouter
from app.schemas import Order
from app.database import order_collection
from app.models import order_helper

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: Order):
    new_order = await order_collection.insert_one(order.dict())
    created_order = await order_collection.find_one({"_id": new_order.inserted_id})
    return order_helper(created_order)

@router.get("/orders/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders_cursor = order_collection.find({"user_id": user_id}).skip(offset).limit(limit).sort("_id")
    orders = []
    async for order in orders_cursor:
        orders.append(order_helper(order))
    return orders
