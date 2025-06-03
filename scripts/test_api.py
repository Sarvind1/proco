import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8000/api/v1"

def test_api():
    # Login
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test endpoints
    endpoints = [
        ("GET", "/products", "List Products"),
        ("GET", "/suppliers", "List Suppliers"),
        ("GET", "/purchase-orders", "List Purchase Orders"),
        ("GET", "/inventory", "List Inventory Movements")
    ]

    for method, endpoint, description in endpoints:
        print(f"\nTesting {description}...")
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        else:
            print(f"Error: {response.text}")

    # Create a new product
    print("\nTesting Create Product...")
    new_product = {
        "sku": "TEST-001",
        "name": "Test Product",
        "description": "A test product",
        "price": 99.99,
        "cost": 49.99,
        "quantity": 10,
        "min_quantity": 2
    }
    response = requests.post(f"{BASE_URL}/products", json=new_product, headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print(f"Created Product: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"Error: {response.text}")

    # Create a new purchase order
    print("\nTesting Create Purchase Order...")
    new_po = {
        "po_number": f"PO-TEST-{datetime.now().strftime('%Y%m%d%H%M')}",
        "supplier_id": 1,
        "status": "draft",
        "total_amount": 299.97,
        "currency": "USD",
        "expected_delivery_date": (datetime.now() + timedelta(days=14)).isoformat(),
        "notes": "Test purchase order",
        "items": [
            {
                "product_id": 1,
                "quantity": 2,
                "unit_price": 99.99,
                "total_price": 199.98
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/purchase-orders", json=new_po, headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print(f"Created Purchase Order: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"Error: {response.text}")

if __name__ == "__main__":
    test_api() 