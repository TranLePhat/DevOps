import requests

def test_hello():
    response = requests.get("http://localhost:5000")
    assert response.text == "Hello CI/CD!"