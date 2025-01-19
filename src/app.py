from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data store
orders = [
    {"id": 1, "item": "Laptop", "quantity": 2, "price": 1200},
    {"id": 2, "item": "Phone", "quantity": 5, "price": 800},
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the demo app!"})

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order["id"] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

@app.route('/orders', methods=['POST'])
def create_order():
    new_order = request.json
    if "id" not in new_order or "item" not in new_order or "quantity" not in new_order or "price" not in new_order:
        return jsonify({"error": "Invalid input"}), 400
    orders.append(new_order)
    return jsonify(new_order), 201

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [order for order in orders if order["id"] != order_id]
    return jsonify({"message": f"Order {order_id} deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)