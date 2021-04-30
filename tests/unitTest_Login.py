import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "instructor"
        pwd = "gounomavs1a"

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
        assert "Logged In successfully"
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
