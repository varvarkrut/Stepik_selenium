from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x.text
y = calc(x)
but2 = browser.find_element(By.CSS_SELECTOR, "#answer")
but2.send_keys(y)
but_submit = browser.find_element(By.CSS_SELECTOR, "[type='submut']")
but_submit.click
#message = browser.find_element_by_id("verify_message")

#assert "successful" in message.text