import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app.api import manager, schemas
from src.app.database import Base, connect_db
from src.app.main import app

if os.path.exists("test.db"):
  os.remove("test.db")

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[connect_db] = override_get_db

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/api/v1/user",
        json={"username": "a", "password": "a", "fullname": "a"},
    )
    assert response.status_code == 201


def test_jwt_token():
    response = client.post(
        "/api/v1/obtain_token",
        json={"username": "a", "password": "a"},
    )
    assert response.status_code == 200


def get_access_token():
    response = client.post(
        "/api/v1/obtain_token",
        json={"username": "a", "password": "a"},
    )
    data = response.json()
    access_token = data.get('access_token')
    return access_token


notification_payload = {"event": "1st-visit", "notification_text": "some text"}


def test_create_notification():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.post(
        "/api/v1/notification",
        json=notification_payload,
        headers=headers,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["event"] == "1st-visit"
    assert data["notification_text"] == "some text"
    assert "id" in data


def test_create_notification_withs_invalid_data():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.post(
        "/api/v1/notification",
        json={"event": "some text"},
        headers=headers,
    )
    assert response.status_code == 422


def test_create_notification_without_access_token():
    response = client.post(
        "/api/v1/notification",
        json=notification_payload
    )
    assert response.status_code == 401


def test_notification_by_id():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get(f"/api/v1/notification/1", headers=headers)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["event"] == "1st-visit"
    assert data["notification_text"] == "some text"
    assert data["id"] == 1


def test_notification_by_invalid_id():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get(f"/api/v1/notification/99999", headers=headers)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Notification does not exist"


def test_notification_by_id_without_access_token():
    response = client.get(f"/api/v1/notification/1")
    assert response.status_code == 401


def test_notification_list():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get(f"/api/v1/notification", headers=headers)
    assert response.status_code == 200, response.text
    data = response.json()
    notification_payload.update({"id": 1})
    assert data == [notification_payload]


def test_notification_list_without_access_token():
    response = client.get(f"/api/v1/notification")
    assert response.status_code == 401


def test_notification_update():
    access_token = get_access_token()
    notification_update_payload = {"notification_text": "updated"}
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.put(f"/api/v1/notification/1",
                          json=notification_update_payload,
                          headers=headers)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["event"] == "1st-visit"
    assert data["notification_text"] == "updated"
    assert data["id"] == 1


def test_notification_update_using_invalid_id():
    access_token = get_access_token()
    notification_update_payload = {"notification_text": "updated"}
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.put(f"/api/v1/notification/999999999",
                          json=notification_update_payload,
                          headers=headers)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Notification does not exist"


def test_notification_update_without_access_token():
    response = client.put(f"/api/v1/notification/1")
    assert response.status_code == 401


def test_notification_delete():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.delete(f"/api/v1/notification/1", headers=headers)
    assert response.status_code == 200


def test_notification_delete_using_invalid_id():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.delete(f"/api/v1/notification/999999999",
                             headers=headers)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Notification does not exist"


def test_notification_delete_without_access_token():
    response = client.delete(f"/api/v1/notification/1")
    assert response.status_code == 401
