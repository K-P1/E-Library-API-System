from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
 
# User Tests
def test_create_user():
    user_data = {"name": "Test User", "email": "testuser@example.com", "is_active": True}
    response = client.post("/user/create", json=user_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_get_user():
    user_id = "us_0001"
    response = client.get(f"/user/{user_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == user_id

def test_get_all_users():
    response = client.get("/user/get/all")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_partial_update_user():
    user_id = "us_0002"
    update_data = {"name": "Updated User"}
    response = client.patch(f"/user/update/{user_id}", json=update_data)
    assert response.status_code in [200, 404, 500]
    if response.status_code == 200:
        assert response.json()["name"] == "Updated User"

def test_full_update_user():
    user_id = "us_0001"
    update_data = {"name": "Updated User", "email": "updateduser@example.com", "is_active": False}
    response = client.put(f"/user/update/{user_id}", json=update_data)
    assert response.status_code in [200, 404, 500]
    if response.status_code == 200:
        assert response.json()["name"] == "Updated User"
        assert response.json()["email"] == "updateduser@example.com"
        assert response.json()["is_active"] == False

def test_deactivate_user():
    user_id = "us_0002"
    response = client.patch(f"/user/deactivate/{user_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["is_active"] == False

def test_delete_user():
    user_id = "us_0003"
    response = client.delete(f"/user/delete/{user_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == user_id


# Book Tests
def test_create_book():
    book_data = {"title": "Test Book", "author": "Test Author", "is_available": True}
    response = client.post("/book/create", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"

def test_get_book():
    book_id = "bk_0001"
    response = client.get(f"/book/get/{book_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == book_id

def test_get_all_books():
    response = client.get("/book/get_all/books")
    assert response.status_code == 200
    #assert len(response.json()) > 0

def test_partial_update_book():
    book_id = "bk_0002"
    update_data = {"title": "Updated Book"}
    response = client.patch(f"/book/update/partial/{book_id}", json=update_data)
    assert response.status_code in [200, 404, 500]
    if response.status_code == 200:
        assert response.json()["title"] == "Updated Book"

def test_full_update_book():
    book_id = "bk_0001"
    update_data = {"title": "Updated Book", "author": "Updated Author", "is_available": False}
    response = client.put(f"/book/update/full/{book_id}", json=update_data)
    assert response.status_code in [200, 404, 500]
    if response.status_code == 200:
        assert response.json()["title"] == "Updated Book"
        assert response.json()["author"] == "Updated Author"
        assert response.json()["is_available"] == False

def test_change_book_availability():
    book_id = "bk_0002"
    book= client.get(f"/book/get/{book_id}")
    response = client.patch(f"/book/change_availability/{book_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["is_available"] == (not book.json()["is_available"])

def test_delete_book():
    book_id = "bk_0003"
    response = client.delete(f"/book/delete/{book_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == book_id

def test_borrow_book():
    record_data = {
        "user_id": "us_0007", 
        "book_id": "bk_0007"}
    response = client.post("/record/borrow", json=record_data)
    assert response.status_code in [200, 404, 400, 403]
    if response.status_code == 200:
        assert response.json()["user_id"] == "us_0007"
        assert response.json()["book_id"] == "bk_0007"
        assert response.json()["is_available"] == False

def test_return_book():
    record_id = "rc_0001"
    update_data = {"returned_at": "2024-12-01"}
    response = client.patch(f"/record/return/{record_id}", json=update_data)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["returned_at"] == "2024-12-01"
        assert response.json()["is_available"] == True


# Record Tests
def test_get_user_record():
    user_id = "us_0007"
    response = client.get(f"/record/get/user/{user_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()[0]["user_id"] == user_id

def test_get_book_record():
    book_id = "bk_0007"
    response = client.get(f"/record/get/book/{book_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()[0]["book_id"] == book_id

def test_get_all_record():
    response = client.get("/record/get/all")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_record():
    record_id = "rc_0001"
    response = client.get(f"/record/get/{record_id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["id"] == record_id