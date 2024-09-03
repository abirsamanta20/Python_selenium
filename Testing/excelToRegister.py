from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
import pandas as pd

# Load data from Excel
file_path = r'E:\Python_Selenium\Part_1\all_data.xlsx'
data = pd.read_excel(file_path)

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

def fill_form(row):
    # Fill the form with data from the given row
    element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[1]/div[1]/input")
    element.clear()
    element.send_keys(row['First Name'])

    element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[1]/div[2]/input")
    element.clear()
    element.send_keys(row['Last Name'])

    element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[2]/div/textarea")
    element.clear()
    element.send_keys(row['Address'])

    element = driver.find_element("xpath", "//*[@id='eid']/input")
    element.clear()
    element.send_keys(row['Email'])

    element = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[4]/div/input")
    element.clear()
    element.send_keys(str(row['Phone']))

    gender = row["Gender"]
    if gender == "Male":
        driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").click()
    elif gender == "Female":
        driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[5]/div/label[2]/input").click()

    hobbies = row["Hobbies"]
    hobby_list = [hobby.strip().lower() for hobby in hobbies.split(',')]
    if "cricket" in hobby_list:
        driver.find_element("xpath", "//*[@id='checkbox1']").click()
    if "movies" in hobby_list:
        driver.find_element("xpath", "//*[@id='checkbox2']").click()
    if "hockey" in hobby_list:
        driver.find_element("xpath", "//*[@id='checkbox3']").click()

    element = driver.find_element("xpath", "//*[@id='msdd']")
    element.click()
    languages = row["Language"]
    language_list = [language.strip() for language in languages.split(',')]
    for lan in language_list:
        option = driver.find_element("xpath", f"//li/a[text()='{lan}']")
        option.click()
    driver.find_element("xpath","//*[@id='basicBootstrapForm']/div[7]/label").click()

    skills_select = Select(driver.find_element("xpath", "//*[@id='Skills']"))
    skills_select.select_by_visible_text(row["Skills"])

    country_dropdown = driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[10]/div/span")
    country_dropdown.click()
    country_option = driver.find_element("xpath", f"//li[contains(text(), '{row['Country']}')]")
    country_option.click()

    Birth_of_birth = row['Dob']
    birth_str = Birth_of_birth.strftime('%m/%d/%Y')
    Emp_Birth = [Birth.strip() for Birth in birth_str.split('/')]

    yearofbirth_select = Select(driver.find_element("xpath", "//*[@id='yearbox']"))
    yearofbirth_select.select_by_visible_text(Emp_Birth[2])

    month_number = Emp_Birth[0]
    month_name = datetime.strptime(month_number, "%m").strftime("%B")
    monthofbirth_select = Select(driver.find_element("xpath", "//*[@id='basicBootstrapForm']/div[11]/div[2]/select"))
    monthofbirth_select.select_by_visible_text(month_name)

    day_value = str(int(Emp_Birth[1]))
    dayofbirth_select = Select(driver.find_element("xpath", "//*[@id='daybox']"))
    dayofbirth_select.select_by_visible_text(day_value)

    element = driver.find_element("xpath", "//*[@id='firstpassword']")
    element.clear()
    element.send_keys(row['Password'])

    element = driver.find_element("xpath", "//*[@id='secondpassword']")
    element.clear()
    element.send_keys(row['Password'])

    time.sleep(3)  # Add a delay to observe the result

# Loop through the rows in the Excel sheet
for index, row in data.iterrows():
    fill_form(row)
    time.sleep(2)  # Pause between rows to observe the process
    driver.refresh()  # Clear the form by refreshing the page
    time.sleep(2)  # Wait for the page to reload

driver.quit()
