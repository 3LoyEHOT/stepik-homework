import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для расчета, взята из задания
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    # 3. Считаем математическую функцию
    y = calc(x)
    
    # 4. Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    
    # 5. Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # 6. Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    # 7. Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    # Даем время скопировать код из консоли
    time.sleep(10)
    browser.quit()