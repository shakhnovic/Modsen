from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://example.com")

    driver.add_cookie({"name": "myCookie", "value": "myValue"})

    cookie = driver.get_cookie("myCookie")
    print(f"Value in cookie: {cookie['value']}")

    driver.delete_cookie("myCookie")

    cookie_after_deletion = driver.get_cookie("myCookie")
    print(f"Value after deletion: {cookie_after_deletion}")

finally:
    driver.quit()
