from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    z = int(a) + int(b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    btn = browser.find_element(By.CLASS_NAME, "btn")
    browser.find_elements
    btn.click()

finally:
    time.sleep(10)
    browser.quit()



