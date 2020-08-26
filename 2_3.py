from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()
x = browser.find_element(By.CSS_SELECTOR, "#input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x)
x = x.text
y = calc(x)
but2 = browser.find_element(By.CSS_SELECTOR, "#answer")
but2.send_keys(y)
but_submit = browser.find_element(By.CSS_SELECTOR, "#solve")
but_submit.click

