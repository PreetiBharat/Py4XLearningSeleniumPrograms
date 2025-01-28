import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click for JS Alert
    js_alert_element = driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]')
    js_alert_element.click()

    WebDriverWait(driver=driver, timeout=2).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You successfully clicked an alert"

    time.sleep(5)


# Click for JS Confirm
def test_Confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    js_confirm_element = driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]')
    js_confirm_element.click()

    time.sleep(2)

    WebDriverWait(driver=driver, timeout=2).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()
    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You clicked: Cancel"

    time.sleep(3)


def test_Prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    js_prompt_element = driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]')
    js_prompt_element.click()

    time.sleep(2)

    WebDriverWait(driver=driver, timeout=2).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Bharat")

    alert.accept()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You entered: Bharat"

    time.sleep(3)
