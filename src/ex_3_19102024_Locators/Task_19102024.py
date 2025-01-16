from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure


def test_Task_AwesomeQA_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # < input
    # type = "text"
    # name = "firstname"
    # value = ""
    # placeholder = "First Name"
    # id = "input-firstname"
    # class ="form-control" >
    first_Name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_Name.send_keys("Preeti")
    time.sleep(2)

    # < input
    # type = "text"
    # name = "lastname"
    # value = ""
    # placeholder = "Last Name"
    # id = "input-lastname"
    # class ="form-control" >
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("Chougule")
    time.sleep(2)

    # < input
    # type = "email"
    # name = "email"
    # value = ""
    # placeholder = "E-Mail"
    # id = "input-email"
    # class ="form-control" >
    email = driver.find_element(By.XPATH, "//input[@id='input-email']")
    email.send_keys("preeti@gmail.com")
    time.sleep(2)

    # < input
    # type = "tel"
    # name = "telephone"
    # value = ""
    # placeholder = "Telephone"
    # id = "input-telephone"
    # class ="form-control" >
    telephone = driver.find_element(By.XPATH, "//input[@name='telephone']")
    telephone.send_keys("1234069876")
    time.sleep(2)

    # < input
    # type = "password"
    # name = "password"
    # value = ""
    # placeholder = "Password"
    # id = "input-password"
    # class ="form-control" >
    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys("Password@1234")
    time.sleep(2)

    # < input
    # type = "password"
    # name = "confirm"
    # value = ""
    # placeholder = "Password Confirm"
    # id = "input-confirm"
    # class ="form-control" >
    password_confirm = driver.find_element(By.XPATH, "//input[@placeholder='Password Confirm']")
    password_confirm.send_keys("Password@1234")
    time.sleep(2)

    # < label
    # class ="radio-inline" >
    # No < input
    # type = "radio"
    # name = "newsletter"
    # value = "0"
    # checked = "checked" >
    # < / label >
    subscribe_button = driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='0']")
    subscribe_button.click()
    time.sleep(2)

    # < input
    # type = "checkbox"
    # name = "agree"
    # value = "1" >
    agree_check_box = driver.find_element(By.XPATH, "//input[@name='agree']")
    agree_check_box.click()
    time.sleep(2)

    # < input
    # type = "submit"
    # value = "Continue"
    # class ="btn btn-primary" >
    continue_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    continue_button.click()
    time.sleep(2)

    source_page = driver.page_source  # find the text on the web page
    assert "Your Account Has Been Created!" in source_page

    # account_created = driver.find_element(by=By.TAG_NAME, value="h1")  # find the X path
    # assert account_created.text == "Your Account Has Been Created!"

    time.sleep(2)
    driver.quit()
