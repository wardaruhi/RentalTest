import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):

        email = "abc"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/form/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/a[2]")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        elem = driver.find_element_by_id("identifierId")
        elem.send_keys(email)
        time.sleep(3)
        assert "Login with gmail page opens, using which the user can signup/login through their gmail account"


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
