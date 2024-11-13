import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_window = browser.window_handles[0]

    first_btn = browser.find_element(By.CLASS_NAME, "trollface")
    first_btn.click()

    # alert = browser.switch_to.alert
    # alert.accept()
    # time.sleep(1)
    browser.switch_to.window(browser.window_handles[1])
    x_el = browser.find_element(By.ID, "input_value")
    print(x_el.text)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(calc(x_el.text))

    btn_2 = browser.find_element(By.CLASS_NAME, "btn")
    btn_2.click()


finally:
    time.sleep(10)
    browser.quit()
