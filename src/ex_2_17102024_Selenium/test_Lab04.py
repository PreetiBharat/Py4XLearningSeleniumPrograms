from selenium import webdriver


def test_task_2_15102024():
    driver = webdriver.Chrome()  # create the session
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to URL
    page_source_data = driver.page_source  # gives the page source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()
