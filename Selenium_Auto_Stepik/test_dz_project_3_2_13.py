import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(self.link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input1.send_keys("Emelyanov")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input1.send_keys("q@net.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка. Не удалось зарегистрироваться")
        browser.quit()

    def test_abs2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(self.link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input1.send_keys("Emelyanov")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input1.send_keys("q@net.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Ошибка. Не удалось зарегистрироваться")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
