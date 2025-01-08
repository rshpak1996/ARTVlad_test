from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Ініціалізація вебдрайвера
driver = webdriver.Chrome()  # Замініть на webdriver.Firefox(), якщо використовуєте Firefox

try:
    # Відкриття сторінки
    driver.get("https://demoqa.com/text-box")

    # Перевірка заголовка сторінки
    assert "Text Box" in driver.title

    # Введення даних у поле Full Name
    full_name_input = driver.find_element(By.ID, "userName")
    full_name_input.send_keys("John Doe")

    # Введення даних у поле Email
    email_input = driver.find_element(By.ID, "userEmail")
    email_input.send_keys("johndoe@example.com")

    # Введення даних у поле Current Address
    current_address_input = driver.find_element(By.ID, "currentAddress")
    current_address_input.send_keys("123 Main Street")

    # Введення даних у поле Permanent Address
    permanent_address_input = driver.find_element(By.ID, "permanentAddress")
    permanent_address_input.send_keys("456 Elm Street")

    # Клік на кнопку "Submit"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Очікування, щоб переконатися, що результат з'явився
    time.sleep(2)

    # Перевірка виведених результатів
    output_name = driver.find_element(By.ID, "name").text
    output_email = driver.find_element(By.ID, "email").text
    output_current_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
    output_permanent_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

    assert "John Doe" in output_name
    assert "johndoe@example.com" in output_email
    assert "123 Main Street" in output_current_address
    assert "456 Elm Street" in output_permanent_address

    print("Тест успішно пройдено!")

except AssertionError as e:
    print("Тест не пройдено:", e)

finally:
    # Закриття браузера
    driver.quit()
