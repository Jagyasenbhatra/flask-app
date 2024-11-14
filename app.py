import pytest
import app  


def test_index():
    """Tests the root route ("/") which returns "Hello!"."""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Hello!"


def test_calculate_success():
    """Tests the "/calc" route with valid integer inputs."""
    with app.test_client() as client:
        response = client.get("/calc?a=5&b=3")
        assert response.status_code == 200
        assert response.data == b"8"


def test_calculate_invalid_input():
    """Tests the "/calc" route with invalid input (non-integers)."""
    with app.test_client() as client:
      
        response = client.get("/calc?a=hello&b=3")
        assert response.status_code == 400  
        assert b"Invalid input" in response.data

        # Test with a string for 'b'
        response = client.get("/calc?a=5&b=world")
        assert response.status_code == 400
        assert b"Invalid input" in response.data


if __name__ == "__main__":
    pytest.main()