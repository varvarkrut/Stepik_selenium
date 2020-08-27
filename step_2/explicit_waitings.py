from selenium import webdriver
import time
import unittest

class MyTestCase(unittest.TestCase):
    def reg(self,cnt): #убрал повторяющиеся действия в отдельную функцию
        link = "http://suninjuly.github.io/registration" + cnt + ".html"
        browser = webdriver.Chrome()
        browser.get(link)

        element_1 = browser.find_element_by_xpath('//input[@class="form-control first"][@required]').send_keys("Ivan")
        element_2 = browser.find_element_by_xpath('//input[@class="form-control second"][@required]').send_keys("Petrov")
        element_3 = browser.find_element_by_xpath('//input[@class="form-control third"][@required]').send_keys("ip@gmail.com")
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         'Всё получилось. Тест пройден')
        browser.quit()

    def test_firstPage(self): #пробуем пройти первый тест
        self.reg('1')

    def test_secondPage(self): #пробуем пройти второй тест
        self.reg('2')

if __name__ == '__main__':
    unittest.main()