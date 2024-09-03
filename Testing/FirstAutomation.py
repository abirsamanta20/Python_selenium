from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/")
driver.maximize_window()
print(driver.title)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.quit()

