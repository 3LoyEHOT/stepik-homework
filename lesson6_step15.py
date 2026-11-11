import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку, которая открывает новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 3. Решаем капчу на новой странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    y = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # 4. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # 5. Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    # Даем время скопировать код из консоли
    time.sleep(10)
    browser.quit()