from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все текстовые поля по тегу input
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждое поле коротким текстом, чтобы успеть до таймера
    for element in elements:
        element.send_keys("1")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(30)
    browser.quit()