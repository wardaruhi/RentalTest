import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_forgotpass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        email = "wmohammadshahabudd@unomaha.edu"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/form/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/a[1]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Forgot Password Email Sent"
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
