import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('location', ["236895", "236896","236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, location):
    link = f"https://stepik.org/lesson/{location}/step/1"
    browser.get(link)
    text_area = browser.find_element(By.TAG_NAME, "textarea")
    text_area.click()
    answer = math.log(int(time.time()))
    text_area.send_keys(str(answer))
    submit_but = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_but.click()
    cor_area = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    area_text = cor_area.text
    assert area_text == "Correct!", f"Wrong! Response is {area_text}"
