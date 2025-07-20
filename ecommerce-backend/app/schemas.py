from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    size: str
    price: float

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    user_id: str
    items: List[OrderItem]
    status: str
