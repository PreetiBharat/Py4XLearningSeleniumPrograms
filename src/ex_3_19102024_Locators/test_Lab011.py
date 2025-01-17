import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Find all the buttons by Tag NAME")
@allure.title("Verify all the elements with TAG NAME")
def test_Project4():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # Tag name
    # buttons = driver.find_elements(By.TAG_NAME, "button")
    # print(len(buttons))  # prints the no of buttons on the current web page
    # for i in buttons:
    #     print(i.text)  # prints all the buttons with its text including space on the current web page

    first_name_input_tag = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name_input_tag.send_keys("Hello")

    time.sleep(5)
    driver.quit()
