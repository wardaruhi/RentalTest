import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class rent_PayPal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):

        number = "1"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("number")
        elem.send_keys(number)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        obj = driver.switch_to.alert
        obj.accept()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]").click()
        time.sleep(5)

        assert "PayPal login pops up where user can fill out their details to proceed with their transaction"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
