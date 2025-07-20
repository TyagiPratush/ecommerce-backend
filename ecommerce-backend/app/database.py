from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGODB_URI")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.ecommerce

product_collection = database.get_collection("products")
order_collection = database.get_collection("orders")
