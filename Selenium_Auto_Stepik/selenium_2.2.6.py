from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.ID, "input_value")

    x = x_el.text
    print(x)
    y = calc(int(x))

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    check_robot = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_robot)
    check_robot.click()
    check_robot = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_robot)
    check_robot.click()

    btn = browser.find_element(By.CLASS_NAME, "btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()


finally:
    time.sleep(5)
    browser.quit()



