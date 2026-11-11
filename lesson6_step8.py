from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Тест должен проходить на этой странице:
link = "http://suninjuly.github.io/registration1.html"

# Для самопроверки: если подставить ссылку ниже, тест должен
# упасть с ошибкой NoSuchElementException — это подтверждает,
# что селекторы уникальны и баг в registration2.html найден.
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Уникальные CSS-селекторы: ищем поля внутри блока .first_block
    # по их уникальным классам .first, .second, .third
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("test@example.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что регистрация прошла успешно
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", \
        f"Ожидали текст успешной регистрации, получили: {welcome_text}"

finally:
    time.sleep(10)
    browser.quit()