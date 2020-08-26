from selenium import webdriver
import time
def test1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".form-group.first_class > input.form-control.first:required")
        input1.send_keys("Vanya")
        input2 = browser.find_element_by_css_selector(".form-group.second_class > input.form-control.second:required")
        input2.send_keys("Shkurko")
        input3 = browser.find_element_by_css_selector(".form-group.third_class > input.form-control.third:required")
        input3.send_keys("vanya.shkurko@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на
        # странице сайта

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
        return welcome_text


def test2():

    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".form-group.first_class > input.form-control.first:required")
    input1.send_keys("Vanya")
    input2 = browser.find_element_by_css_selector(".form-group.second_class > input.form-control.second:required")
    input2.send_keys("Shkurko")
    input3 = browser.find_element_by_css_selector(".form-group.third_class > input.form-control.third:required")
    input3.send_keys("vanya.shkurko@mail.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на
    # странице сайта

    # ожидание чтобы визуально оценить результаты прохождения скрипта

    # закрываем браузер после всех манипуляций
    return welcome_text