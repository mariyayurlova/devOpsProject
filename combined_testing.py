import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from db_connector import create_connection

def test_combined():
    user_id = 123
    user_name = "Maria"

    response = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={'user_name': user_name})
    assert response.status_code == 200, "POST request failed"

    response = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    assert response.status_code == 200 and response.json()['user_name'] == user_name, "GET request failed"

    conn = create_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT user_name FROM users WHERE user_id=%s", (user_id,))
        result = cursor.fetchone()
        assert result['user_name'] == user_name, "DB check failed"

    driver = webdriver.Chrome(service=Service("/Users/maria/Downloads/chromedriver-mac-x64/chromedriver"))
    driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
    user_name_element = driver.find_element(By.ID, value='user_name')
    assert user_name_element.text == user_name, "Web interface check failed"
    driver.quit()

if __name__ == '__main__':
    test_combined()