import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем зашифрованный текст ссылки: 224592
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    # Находим ссылку по тексту и кликаем
    link_element = browser.find_element(By.LINK_TEXT, link_text)
    link_element.click()

    # Заполняем форму так же, как в предыдущем задании
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Получаем проверочный код из всплывающего окна
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(30)
    browser.quit()