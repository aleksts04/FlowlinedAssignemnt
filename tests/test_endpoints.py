from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summarize():
    response = client.post("/api/summarize", json={"text": "OpenAI builds advanced AI systems."})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert isinstance(response.json()["summary"], str)

def test_similarity():
    data = {
        "query": "AI development",
        "texts": [
            "Football is fun.",
            "OpenAI builds AI models.",
            "Cooking is a great skill."
        ]
    }
    response = client.post("/api/similarity", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert "closest_text" in json_data
    assert "score" in json_data
    assert isinstance(json_data["closest_text"], str)
    assert isinstance(json_data["score"], float)

def test_summarize_missing_text():
    response = client.post("/api/summarize", json={})
    assert response.status_code == 422  # Validation error from Pydantic

def test_summarize_empty_text():
    response = client.post("/api/summarize", json={"text": ""})
    assert response.status_code == 200  # Depends on your backend logic
    assert "summary" in response.json()

def test_similarity_missing_query():
    response = client.post("/api/similarity", json={"texts": ["A", "B"]})
    assert response.status_code == 422

def test_similarity_missing_texts():
    response = client.post("/api/similarity", json={"query": "Some query"})
    assert response.status_code == 422

def test_similarity_invalid_texts_type():
    response = client.post("/api/similarity", json={"query": "Some query", "texts": "not a list"})
    assert response.status_code == 422

def test_similarity_empty_texts_list():
    response = client.post("/api/similarity", json={"query": "test", "texts": []})
    # Depending on your backend error handling, this could be 422 or 500
    assert response.status_code in (422, 500)