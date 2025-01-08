import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(chrome_options)  # create the session
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to URL
    # chrome # Incognito mode

    assert True == False

    time.sleep(10)
