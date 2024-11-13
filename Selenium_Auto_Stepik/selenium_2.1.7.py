from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.CSS_SELECTOR, "#treasure")

    x = x_el.get_attribute("valuex")
    print(x)
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()


    check_robot = browser.find_element(By.ID, "robotsRule")
    check_robot.click()
    time.sleep(2)

    btn = browser.find_element(By.CLASS_NAME, "btn")
    btn.click()


finally:
    time.sleep(5)
    browser.quit()



