from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    cur_dir = (os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(cur_dir, 'text.txt')
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fsname_el = browser.find_element_by_css_selector("[name='firstname']")
    fsname_el.send_keys("Ivan")
    lsname_el = browser.find_element_by_css_selector("[name='lastname']")
    lsname_el.send_keys("Shkurko")
    mail_el = browser.find_element_by_css_selector("[name='email']")
    mail_el.send_keys("vanya.shcurko@gmail.com")
    file_el = browser.find_element_by_css_selector("[type='file']")
    file_el.send_keys(file_path)
    but3 = browser.find_element_by_css_selector("[type='submit']")
    but3.click()
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
