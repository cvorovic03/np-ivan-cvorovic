from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item_success():
    response = client.post("/items/1", json={"name": "Laptop", "price": 1200.0, "quantity": 1})
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "Laptop"

def test_read_item_success():
    client.post("/items/2", json={"name": "Mis", "price": 25.0})
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Mis"

def test_read_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_create_duplicate_item():
    client.post("/items/3", json={"name": "Tastatura", "price": 50.0})
    response = client.post("/items/3", json={"name": "Tastatura 2", "price": 60.0})
    assert response.status_code == 400

def test_create_item_negative_price():
    response = client.post("/items/4", json={"name": "Slusalice", "price": -10.0})
    assert response.status_code == 422

def test_create_item_zero_price():
    response = client.post("/items/4", json={"name": "Slusalice", "price": 0.0})
    assert response.status_code == 422

def test_create_item_short_name():
    response = client.post("/items/5", json={"name": "A", "price": 10.0})
    assert response.status_code == 422

def test_create_item_invalid_type():
    response = client.post("/items/6", json={"name": "Monitor", "price": "sto dinara"})
    assert response.status_code == 422
