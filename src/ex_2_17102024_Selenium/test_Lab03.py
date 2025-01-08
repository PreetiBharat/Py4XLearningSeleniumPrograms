from selenium import webdriver


def test_open_vwo_login():
    driver = webdriver.Chrome()  # create the session
    driver.get("https://app.vwo.com")  # Navigate to URL
    page_source_data = driver.page_source  # gives the page source
    print(page_source_data)
