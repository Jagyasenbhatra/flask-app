
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
        assert response.data==b'{"result":8}\n' 


def test_calculate_invalid():
        with app.test_client() as client:
            response = client.get("/calc?a=hello&b=3")
            assert response.status_code == 400  
            assert response.data==b'{"error":"Invalid input"}\n' 

            res=client.get("/calc?a=3&b=hello")
            assert res.status_code==400
            assert res.data==b'{"error":"Invalid input"}\n' 


if __name__ == "__main__":
    pytest.main()