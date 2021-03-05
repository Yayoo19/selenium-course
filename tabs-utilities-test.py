import unittest
from selenium import webdriver
# from selenium.webdriver.common import keys


# Switching between tabs

class TabsUnitTest(unittest.TestCase):

    def test_changeWindow(self):
        driver = webdriver.Firefox(executable_path=r"C:\Tools\geckodriver.exe")
        driver.get("https://www.google.com")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://wikipedia.com")
        driver.switch_to.window(driver.window_handles[0])


if __name__ == '__main__':
    TabsUnitTest.main()