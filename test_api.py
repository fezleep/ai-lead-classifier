import requests

def test_classifier():
    url = "http://localhost:8000/analyze-lead"
    data = {
        "name": "Alice Smith",
        "message": "I'm just browsing, not looking to buy anything right now."
    }

    try:
        response = requests.post(url, json=data)
        print(f"Status: {response.status_code}")
        print(f"Result: {response.json()}")
    except Exception as e:
        print(f"Error: {e}. Make sure your API is running (uvicorn app.main:app)")

if __name__ == "__main__":
    test_classifier()