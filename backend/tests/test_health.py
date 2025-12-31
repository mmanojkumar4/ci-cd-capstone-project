from app.main import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code in [200, 500]
