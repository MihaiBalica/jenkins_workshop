orders = [
    {"id": 1, "item": "Laptop", "quantity": 2, "price": 1200},
    {"id": 2, "item": "Phone", "quantity": 5, "price": 800},
]

def get_all_orders():
    return orders

def get_order_by_id(order_id):
    return next((order for order in orders if order["id"] == order_id), None)

def add_order(order):
    orders.append(order)

def delete_order_by_id(order_id):
    global orders
    orders = [order for order in orders if order["id"] != order_id]