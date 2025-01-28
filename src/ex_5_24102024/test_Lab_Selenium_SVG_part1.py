import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("Verify SVG")
def test_svg_alerts():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("mac mini")

    list_svg = driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg[0].click()

    time.sleep(3)
