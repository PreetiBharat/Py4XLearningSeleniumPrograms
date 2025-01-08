import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_make_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # 1- Find the element
    # <a - open tag-the anchor tag
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a> - close tag

    # Find an element given a By strategy and locator.
    # 2- We need to find the unique attribute which can find the web element

    make_appointment_element = driver.find_element(By.ID, value="btn-make-appointment")

    # 3- Click on it
    make_appointment_element.click()

    # 4- Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()
