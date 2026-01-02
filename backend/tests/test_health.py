import sys
sys.path.append("/app")

from app.main import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200