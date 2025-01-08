import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_task2_make_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element = driver.find_element(By.ID, value="btn-make-appointment")

    make_appointment_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username_element = driver.find_element(By.ID, value="txt-username")

    username_element.send_keys()

    password_element = driver.find_element(By.ID, value="txt-password")

    password_element.send_keys()

    login_element = driver.find_element(By.ID, value="btn-login")
    login_element.click()

    time.sleep(5)
    driver.quit()
