from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


def test_different_localizations(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(15)
    browser.get(link)
    try:
        bucket_but = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except NoSuchElementException:
        bucket_but = False
    assert bucket_but != False, "Test failed, button was not found!"
