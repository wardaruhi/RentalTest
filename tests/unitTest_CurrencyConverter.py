import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class rent_currencyconverter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "test2"
        pwd = "maverick1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/form/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("userMenu")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[5]/h4/div/a[1]")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        obj = Select(driver.find_element_by_name("view_currency"))
        obj.select_by_index(1)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Currency converted successfully"


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
