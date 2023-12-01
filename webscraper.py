from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.marketwatch.com/investing/index/spx"

driver = webdriver.Chrome()
driver.get(url)

data = driver.find_element(By.CLASS_NAME, 'value')