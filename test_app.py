
import pytest
from main import app

def test_index():
  
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Hello!"


def test_calculate_success():
   
    with app.test_client() as client:
        response = client.get("/calc?a=5&b=3")
        assert response.status_code == 200
        assert response.data == b"8"


if __name__ == "__main__":
    pytest.main()