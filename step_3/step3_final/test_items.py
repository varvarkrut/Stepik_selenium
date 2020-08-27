from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


def test_different_localizations(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(15)
    browser.get(link)
    try:
        submit_but = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except:
        submit_but = False
    submit_but.click()
    assert submit_but != False, "Test failed, button was not found!"
