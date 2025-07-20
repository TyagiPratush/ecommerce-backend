def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "size": product["size"],
        "price": product["price"]
    }

def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "items": order["items"],
        "status": order["status"]
    }
