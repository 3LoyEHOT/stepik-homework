import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 2. Считаем функцию
    y = calc(x)

    # 3. Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # 4. Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    # Прокручиваем к чекбоксу, чтобы он не был перекрыт футером
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    # 5. Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    # Прокручиваем к радиокнопке
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # 6. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Прокручиваем к кнопке, так как она перекрыта футером
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # 7. Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()