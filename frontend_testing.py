from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_web_interface(user_id):
    driver = webdriver.Chrome(service=Service("/Users/maria/Downloads/chromedriver-mac-x64/chromedriver"))
    driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')
    user_name_element = driver.find_element(By.ID, value='user_name')
    print(user_name_element.text)
    driver.quit()

if __name__ == '__main__':
    test_web_interface(1)