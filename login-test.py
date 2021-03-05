from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Using webdriver
driver =webdriver.Firefox(executable_path=r"C:\Tools\geckodriver.exe")
driver.get("https://github.com/login")
time.sleep(3)

# Find element in webpage
user = driver.find_element_by_id("login_field")
# write and enter on that element found
user.send_keys("chavezjorgeeduardo19@gmail.com")
user.send_keys(Keys.ENTER)

# Find element, put info and press enter
pw = driver.find_element_by_name("password")
pw.send_keys("12345")
pw.send_keys(Keys.ENTER)


