import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")

    # 2. Формируем путь к файлу (он должен лежать в той же папке, что и скрипт)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    # 3. Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 5. Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()