import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ждем, пока цена не станет $100 (таймаут 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Решаем математическую задачу на новой странице
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # 4. Отправляем решение
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # 5. Получаем проверочный код
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()