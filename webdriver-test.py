from selenium import webdriver

# Trying driver functionality
driver = webdriver.Firefox(executable_path=r"C:\Tools\geckodriver.exe")
driver.get(r"http://github.com")
driver.close()

