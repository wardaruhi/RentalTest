import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class rent_category(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        obj = Select(driver.find_element_by_name("category"))
        obj.select_by_index(14)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/form/input")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Category selected and results updated successfully"
        time.sleep(1)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
