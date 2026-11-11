import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
# Для проверки на второй странице раскомментируйте строку ниже и закомментируйте верхнюю
# link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем числа со страницы и приводим их к целым числам
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    # 2. Считаем сумму и сразу преобразуем её в строку (это важно для поиска в списке)
    total = str(num1 + num2)

    # 3. Инициализируем объект Select и выбираем значение, равное сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total)

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