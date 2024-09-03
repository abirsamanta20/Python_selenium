from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
print(driver.title)
assert "Register" in driver.title

element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[1]/div[1]/input")

# elem.clear()
element.send_keys("Abir")

element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[1]/div[2]/input")
element.send_keys("Samanta")

element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[2]/div/textarea")
element.send_keys("Unit - 9ES5, Mani Casadona, Action Area - IIF, Newtown, Kolkata, West Bengal 700156, India")

element = driver.find_element("xpath", "//*[@id='eid']/input")
element.send_keys("abirsamanta871@gmail.com")

element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[4]/div/input")
element.send_keys("4521789654")


male_radio_button = driver.find_element("xpath","//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input")
female_radio_button = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[5]/div/label[2]/input")


gender = "Male" 

if gender == "Male":
    male_radio_button.click()
elif gender == "Female":
    female_radio_button.click()
else:
    print("Invalid gender provided")

cricket_radio_button = driver.find_element("xpath","//*[@id='checkbox1']")
movies_radio_button = driver.find_element("xpath","//*[@id='checkbox2']")
hockey_radio_button = driver.find_element("xpath","//*[@id='checkbox3']")

hobbies ="hockey"

if hobbies == "cricket":
    cricket_radio_button.click()
elif hobbies == "movies":
    movies_radio_button.click()
elif hobbies == "hockey":
    hockey_radio_button.click()
else:
    print("Invalid hobbies provided")

 

element = driver.find_element("xpath", "//*[@id='msdd']")
# element = driver.find_element("xpath", "//*[@id='msdd']")
time.sleep(5)

languages = ["English", "Hindi","Arabic"]

element = driver.find_element("xpath", "//*[@id='msdd']")
element.click()

# Loop through each language and select the corresponding option
for language in languages:
    # Find the option based on the value of the language variable
    option = driver.find_element("xpath", f"//li/a[text()='{language}']")
    option.click()

outside = driver.find_element("xpath","//*[@id='basicBootstrapForm']/div[7]/label")
outside.click()



skills_dropdown = driver.find_element("xpath", "//*[@id='Skills']")
skills_select = Select(skills_dropdown)

skills_select.select_by_visible_text("Python")

country_dropdown = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[10]/div/span")
country_dropdown.click()
time.sleep(3)

country_option = driver.find_element("xpath", "//li[contains(text(), 'India')]")
country_option.click()
yearofbirth_dropdown = driver.find_element("xpath", "//*[@id='yearbox']")
yearofbirth_select = Select(yearofbirth_dropdown)

yearofbirth_select.select_by_visible_text("2000")

monthofbirth_dropdown = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[11]/div[2]/select")
monthofbirth_select = Select(monthofbirth_dropdown)

monthofbirth_select.select_by_visible_text("February")

dayofbirth_dropdown = driver.find_element("xpath", "//*[@id='daybox']")
dayofbirth_select = Select(dayofbirth_dropdown)

dayofbirth_select.select_by_visible_text("20")

element = driver.find_element("xpath", "//*[@id='firstpassword']")
element.send_keys("abir@2000")

element = driver.find_element("xpath", "//*[@id='secondpassword']")
element.send_keys("abir@2000")

assert "No results found." not in driver.page_source 
driver.quit()
time.sleep(5)