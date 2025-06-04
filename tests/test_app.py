import os
import requests

def test_homepage_status():
    url = os.environ.get("API_URL", "http://localhost:5000") + "/"
    response = requests.get(url)
    assert response.status_code == 200

def test_contact_status():
    url = os.environ.get("API_URL", "http://localhost:5000") + "/contact/"
    response = requests.get(url)
    assert response.status_code == 200

def test_exercices_status():
    url = os.environ.get("API_URL", "http://localhost:5000") + "/exercices/"
    response = requests.get(url)
    assert response.status_code == 200
