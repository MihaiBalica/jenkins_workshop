import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the demo app!" in response.data

def test_get_orders(client):
    response = client.get('/orders')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_create_order(client):
    new_order = {"id": 3, "item": "Tablet", "quantity": 3, "price": 600}
    response = client.post('/orders', json=new_order)
    assert response.status_code == 201
    assert response.json == new_order

def test_delete_order(client):
    response = client.delete('/orders/1')
    assert response.status_code == 200
    assert b"Order 1 deleted" in response.data