import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class WaitUnitTest(unittest.TestCase):

    def test_explicitWait(self):
        driver = webdriver.Firefox(executable_path=r"C:\Tools\geckodriver.exe")
        driver.get("http://www.google.com")
        try:
            # Waiting for element in the page to be found
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
            component = driver.find_element_by_name("q")
            component.send_keys("AMD")
            component.send_keys(Keys.ENTER)
        finally:
            driver.close()


if __name__ == '__main__':
    WaitUnitTest.main()