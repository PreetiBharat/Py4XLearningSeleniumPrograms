import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Find all the buttons by Tag NAME")
@allure.title("Verify all the elements with TAG NAME")
def test_Project4():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # Tag name
    # buttons = driver.find_elements(By.TAG_NAME, "button")
    # print(len(buttons))  # prints the no of buttons on the current web page
    # for i in buttons:
    #     print(i.text)  # prints all the buttons with its text including space on the current web page

    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links))  # prints the no of links on the current web page
    for i in all_links:
        print(i.text)  # prints all the links with its text including space on the current web page

    time.sleep(5)
    driver.quit()
