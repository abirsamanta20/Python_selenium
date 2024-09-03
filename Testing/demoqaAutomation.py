from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
assert "DEMOQA" in driver.title

textbox = driver.find_element("xpath", "//*[@id='item-0']")
textbox.click()

Nameelement = driver.find_element("xpath", "//*[@id='userName']")
Nameelement.send_keys("Abir Samanta")

Gmailelement = driver.find_element("xpath", "//*[@id='userEmail']")
Gmailelement.send_keys("abirsamanta58752@gmail.com")

currentaddresselement = driver.find_element("xpath", "//*[@id='currentAddress']")
currentaddresselement.send_keys("New Town, Kolkata, West Bengal")
time.sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

parmanentaddresselement = driver.find_element("xpath", "//*[@id='permanentAddress']")
parmanentaddresselement.send_keys("Purba Medinipur, West Bengal-721144")

time.sleep(3)
submit_button = driver.find_element("xpath", "//*[@id='submit']")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
submit_button.click()
time.sleep(4)

# driver.back()

# Now you can interact with the checkbox
checkbox = driver.find_element("xpath", "//*[@id='item-1']")
checkbox.click()

time.sleep(3)

homebox = driver.find_element("xpath", "//*[@id='tree-node']/ol/li/span/label")
# homebox.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
if not homebox.is_selected():
    homebox.click()
time.sleep(2)


checkbox = driver.find_element("xpath", "//*[@id='item-2']")
checkbox.click()
# time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

click_redio = "Yes" 


if click_redio == "Yes":
    yes_radio_button = driver.find_element("xpath","//*[@id='app']/div/div/div/div[2]/div[2]/div[2]")
    yes_radio_button.click()
    time.sleep(6)
elif click_redio == "Impressive":
    impressive_radio_button = driver.find_element("xpath", "//*[@id='app']/div/div/div/div[2]/div[2]/div[3]")
    impressive_radio_button.click()
else:
    print("Invalid gender provided")

print(driver.title)

# assert "No results found." not in driver.page_source   
# driver.quit()