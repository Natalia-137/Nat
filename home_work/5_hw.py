from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

name = driver.find_element(By.CSS_SELECTOR, '#user-name')

password = driver.find_element(By.CSS_SELECTOR, '#password')

button_submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

if not button_submit is None and not name is None and not password is None:
    print('Элементы найдены')
else:
    print('Не вышло')
