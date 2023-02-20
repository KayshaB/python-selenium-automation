from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/thematrix/Desktop/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


driver = webdriver.Chrome(executable_path='/Users/thematrix/Desktop/python-selenium-automation/chromedriver')

driver.get('http://www.amazon.com/')
driver.find_element(By.ID, "nav-orders").click()
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but actually got {actual_result}'
print('Passed')

driver.quit()