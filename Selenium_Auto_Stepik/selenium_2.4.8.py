import math
import time
from os import times

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    x_el = browser.find_element(By.ID, "input_value")
    print(x_el.text)
    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(calc(x_el.text))
    btn_2 = browser.find_element(By.ID, "solve")
    btn_2.click()

finally:
    time.sleep(5)
    browser.quit()
