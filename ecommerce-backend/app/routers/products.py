from fastapi import APIRouter, Query
from app.schemas import Product
from app.database import product_collection
from app.models import product_helper
from bson import ObjectId

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: Product):
    new_product = await product_collection.insert_one(product.dict())
    created_product = await product_collection.find_one({"_id": new_product.inserted_id})
    return product_helper(created_product)

@router.get("/products")
async def list_products(
        name: str = None,
        size: str = None,
        limit: int = 10,
        offset: int = 0
    ):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    products_cursor = product_collection.find(query).skip(offset).limit(limit).sort("_id")
    products = []
    async for product in products_cursor:
        products.append(product_helper(product))
    return products
