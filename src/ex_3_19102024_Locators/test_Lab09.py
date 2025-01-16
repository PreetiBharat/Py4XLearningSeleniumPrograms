import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Verify that Free Trial button is clicked and navigated to next page")
@allure.title("Verify the negative Tc for login to app.vwo.com for invalid UN, PW and error message")
def test_vwo_Free_trial_Project3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # LINK_TEXT = EXACT Match
    start_Free_trial_link = driver.find_element(By.LINK_TEXT, "Start a free trial")
    start_Free_trial_link.click()

    # PARTIAL_LINK_TEXT - means 'contains'
    # anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    # anchor_tag_element.click()

    assert driver.current_url == ("https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign"
                                  "=mof_eg_loginpage")

    driver.back()

    time.sleep(5)
    driver.quit()
