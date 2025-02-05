import pytest
import requests

#  & "c:/Formacion Python/.venv/Scripts/python.exe" -m pytest "c:/Formacion Python/ejerApiPetStore.py" -v

BASE_URL = "https://petstore3.swagger.io/api/v3"

VALID_PET = {
    "id": 1111111,
    "name": "Michi",
    "category": {"id": 2, "name": "Gatos"},
    "photoUrls": ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg"],
    "tags": [{"id": 1, "name": "tímido"}],
    "status": "available"
}

INVALID_PET = {
    "id": True,
    "name": "Michi", 
    "photoUrls": ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg"],
    "tags": [{"id": 1, "name": "tímido"}],
    "status": "available"
}

def test_post_pet_success():
    response = requests.post(f"{BASE_URL}/pet", json=VALID_PET, headers={"Content-Type": "application/json"})
    assert response.status_code == 200, f"Error: Expected status code 200, but received {response.status_code}"
    assert response.json()["id"] == VALID_PET["id"], "The registered pet ID does not match the expected one."
    assert "name" in response.json(), "The pet name is missing in the response."
    assert response.json()["status"] == "available", "The pet status is not as expected."

def test_post_pet_failure():
    response = requests.post(f"{BASE_URL}/pet", json=INVALID_PET, headers={"Content-Type": "application/json"})
    assert response.status_code == 400, f"Error: Expected status code 400, but received {response.status_code}"
    if response.text.strip():
        json_response = response.json()
        assert "message" in json_response, "No error message was received in the response."
        print(f"Error message received: {json_response['message']}")
    else:
        print("The API did not return any error message when one was expected.")

def test_get_pet_by_id():
    response = requests.get(f"{BASE_URL}/pet/{VALID_PET['id']}")
    assert response.status_code == 200, f"Error: Expected status code 200, but received {response.status_code}"
    assert response.json()["id"] == VALID_PET["id"], "The retrieved pet ID does not match the expected one."
    assert "category" in response.json(), "The response does not include the pet's category."
    assert response.json()["status"] == "available", "The pet status is not as expected."

def test_update_pet():
    updated_pet = VALID_PET.copy()
    updated_pet["name"] = "Zarpas"
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet, headers={"Content-Type": "application/json"})
    assert response.status_code == 200, f"Error: Expected status code 200, but received {response.status_code}"
    assert response.json()["name"] == "Zarpas", "The pet name was not updated correctly."
    assert "name" in response.json(), "The updated pet name is missing in the response."
    assert response.json()["status"] == "available", "The pet status is not as expected after the update."

def test_delete_pet():
    response = requests.delete(f"{BASE_URL}/pet/{VALID_PET['id']}")
    assert response.status_code == 200, f"Error: Expected status code 200, but received {response.status_code}"
    response = requests.get(f"{BASE_URL}/pet/{VALID_PET['id']}")
    assert response.status_code == 404, "Error: The pet was not deleted successfully. It still exists in the database."
