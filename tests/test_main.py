from fastapi.testclient import TestClient
from main import app
from services import fake_data

fake_data.generate_initial_data()

client = TestClient(app)


# User Tests
def test_create_user():
    user_data = {"name": "Test User", "email": "testuser@example.com", "is_active": True}
    response = client.post("/user/create", json=user_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_get_user():
    user_id = "us_1001"
    response = client.get(f"/user/get/{user_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == user_id

def test_update_user():
    user_id = "us_1002"
    update_data = {"name": "Updated User"}
    response = client.patch(f"/user/update/{user_id}", json=update_data)
    assert response.status_code in [200, 404, 500]
    if response.status_code == 200:
        assert response.json()["name"] == "Updated User"

def test_delete_user():
    user_id = "us_1003"
    response = client.delete(f"/user/delete/{user_id}")
    assert response.status_code in [200, 404]


# Book Tests
def test_create_book():
    book_data = {"title": "Test Book", "author": "Test Author", "is_available": True}
    response = client.post("/book/create", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"

def test_get_book():
    book_id = "bk_1001"
    response = client.get(f"/book/get/{book_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == book_id

def test_update_book():
    book_id = "bk_1002"
    update_data = {"title": "Updated Book"}
    response = client.patch(f"/book/update/{book_id}", json=update_data)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["title"] == "Updated Book"

def test_delete_book():
    book_id = "bk_1003"
    response = client.delete(f"/book/delete/{book_id}")
    assert response.status_code in [200, 404]


# Record Tests
def test_create_record():
    record_data = {"user_id": "us_1001", "book_id": "bk_1001"}
    response = client.post("/record/create", json=record_data)
    assert response.status_code == 201

def test_get_record():
    record_id = "rc_1001"
    response = client.get(f"/record/get/{record_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == record_id

def test_update_record():
    record_id = "rc_1001"
    update_data = {"returned_at": "2023-12-01"}
    response = client.patch(f"/record/update/{record_id}", json=update_data)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["returned_at"] == "2023-12-01"