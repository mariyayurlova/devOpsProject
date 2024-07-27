import requests

def test_rest_api():
    user_id = 3
    user_name = "elly"

    response = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={'user_name': user_name})
    print(f"POST response: {response.status_code}, {response.json()}")
    assert response.status_code == 200, "POST request failed"

    response = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    print(f"GET response: {response.status_code}, {response.json()}")
    assert response.status_code == 200 and response.json()['user_name'] == user_name, "GET request failed"

    new_user_name = "124"
    response = requests.put(f'http://127.0.0.1:5000/users/{user_id}', json={'user_name': new_user_name})
    assert response.status_code == 200, "PUT request failed"

    response = requests.delete(f'http://127.0.0.1:5000/users/{user_id}')
    assert response.status_code == 200, "DELETE request failed"

if __name__ == '__main__':
    test_rest_api()