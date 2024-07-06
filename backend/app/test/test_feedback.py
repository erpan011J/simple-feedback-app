# test_api.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_feedback():
    """Test creating feedback via API."""
    feedback_data = {"score": 5, "comment": "Great feedback!"}
    response = client.post("/feedback/", json=feedback_data)
    assert response.status_code == 200
    created_feedback = response.json()
    assert created_feedback["score"] == feedback_data["score"]
    assert created_feedback["comment"] == feedback_data["comment"]

def test_create_feedback_invalid_score():
    """Test creating feedback with an invalid score."""
    feedback_data = {"score": 6, "comment": "Too high score!"}
    response = client.post("/feedback/", json=feedback_data)
    assert response.status_code == 400
    assert "Score must be between 1 and 5" in response.text

def test_create_feedback_missing_data():
    """Test creating feedback with missing data."""
    feedback_data = {"comment": "Missing score!"}
    response = client.post("/feedback/", json=feedback_data)
    assert response.status_code == 422
    assert "value_error.missing" in response.text