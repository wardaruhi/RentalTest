import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_address(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "test2"
        pwd = "maverick2a"
        add = "1234 Street"
        zip = "1234"
        city = "Omaha"
        state = "NE"
        country = "USA"
        add2 = "6789 Street"

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
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[2]/h4/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_address1")
        elem.send_keys(add)
        time.sleep(1)
        elem = driver.find_element_by_id("id_zip_code")
        elem.send_keys(zip)
        time.sleep(1)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys(city)
        time.sleep(1)
        elem = driver.find_element_by_id("id_state")
        elem.send_keys(state)
        time.sleep(1)
        elem = driver.find_element_by_id("id_country")
        elem.send_keys(country)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[2]/h4/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/p/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("id_address1").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_address1")
        elem.send_keys(add2)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Address added and edited/updated"

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
