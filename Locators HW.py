from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service = Service('/Users/thematrix/Desktop/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


driver = webdriver.Chrome(executable_path='/Users/thematrix/Desktop/python-selenium-automation/chromedriver')

driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']" )
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "continue")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")
driver.find_element(By.ID, "createAccountSubmit")
driver.find_element(By.XPATH,"//a[contains(@href,'cou?')]")
driver.find_element(By.XPATH, "//a[contains(@href,'privacy') and @rel='noopener']")
