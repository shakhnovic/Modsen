from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Установите опции Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Опционально, для запуска в фоновом режиме

# Укажите путь к ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# Запустите браузер
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Откройте веб-страницу
    driver.get("https://example.com")

    # Установите значение в LocalStorage
    driver.execute_script("localStorage.setItem('myKey', 'myValue');")

    # Получите значение из LocalStorage
    value = driver.execute_script("return localStorage.getItem('myKey');")
    print(f"Value in LocalStorage: {value}")

    # Удалите значение из LocalStorage
    driver.execute_script("localStorage.removeItem('myKey');")

    # Проверьте, что значение удалено
    value_after_deletion = driver.execute_script("return localStorage.getItem('myKey');")
    print(f"Value after deletion: {value_after_deletion}")

finally:
    # Закройте браузер
    driver.quit()
