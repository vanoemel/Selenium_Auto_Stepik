from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)
try:

    button = browser.find_element(By.ID, "button")



finally:
    time.sleep(3)
    browser.quit()