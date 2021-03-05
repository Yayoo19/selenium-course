import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ExampleUnitTest(unittest.TestCase):

# Search a word in the title of the page
    def test_search(self):
        driver = self.driver = webdriver.Firefox(executable_path=r"C:\Tools\geckodriver.exe")
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        element = driver.find_element_by_name("q")
        element.send_keys("Selenium")
        element.send_keys(Keys.ENTER)
        assert "No element found in" not in driver.page_source # in case the word isn't found it sends this assert.
        driver.close()
# End of test case


if __name__ == '__main__':
    ExampleUnitTest.main()

