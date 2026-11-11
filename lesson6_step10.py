import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим картинку сундука и берем значение атрибута valuex
    treasure = browser.find_element(By.ID, "treasure")
    x_value = treasure.get_attribute("valuex")

    # 2. Считаем функцию
    y = calc(x_value)

    # 3. Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # 4. Отмечаем чекбокс "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 5. Выбираем радиокнопку "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 6. Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 7. Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()