import requests

def create_folder(folder_name):
    headers = {
        "Authorization": Token,  
        "Content-Type": "application/json"
    }
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {
        "path": folder_name
    }
    response = requests.put(url, headers=headers, params=params)
    return response

def test_create_folder_positive():
    folder_name = "TestFolder"
    response = create_folder(folder_name)
    assert response.status_code == 201
    assert folder_name in requests.get("https://cloud-api.yandex.net/v1/disk/resources", headers={"Authorization": Token}).json()["items"]

def test_create_folder_negative_already_exists():
    folder_name = "TestFolder"
    create_folder(folder_name)
    response = create_folder(folder_name)
    assert response.status_code == 409

def test_create_folder_negative_no_name():
    response = create_folder("")
    assert response.status_code == 400

