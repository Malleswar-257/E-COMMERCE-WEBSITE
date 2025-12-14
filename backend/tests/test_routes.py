from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post('/api/register', json={'email': 'user@example.com', 'password': 'password'})
    assert response.status_code == 200
    assert response.json()['}'
]