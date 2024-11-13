import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
print(os.path.abspath(__file__))
print(current_dir)
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element(By.NAME, "firstname")
    fn.send_keys("Ivan")

    ln = browser.find_element(By.NAME, "lastname")
    ln.send_keys("Em")

    em = browser.find_element(By.NAME, "email")
    em.send_keys("q@net.ru")

    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)

    btn = browser.find_element(By.CLASS_NAME, "btn")
    btn.click()
finally:
    time.sleep(10)
    browser.quit()