import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@pytest.mark.negative
@allure.description("Verify the error message is displayed when wrong UN and PW is entered")
@allure.title("Verify the negative Tc for login to app.vwo.com for invalid UN, PW and error message")
def test_Negative_vwo_login_Project2():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # Find the username,
    # Find the password
    # login and enter UN and PW
    username_web_element = driver.find_element(By.ID, "login-username")
    username_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.ID, "login-password")
    password_web_element.send_keys("password@1234")
    time.sleep(3)
    # Sign In button web element
    sign_in_button = driver.find_element(By.ID, "js-login-btn")
    # Wait for sometime
    time.sleep(3)

    # error message verification
    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()
