import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку, которая вызывает confirm
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Переключаемся на модальное окно и принимаем его
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. На новой странице считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 4. Считаем функцию и вводим ответ
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # 5. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # 6. Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    # Даем время скопировать код из консоли
    time.sleep(10)
    browser.quit()