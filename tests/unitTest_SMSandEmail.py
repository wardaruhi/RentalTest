import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_contact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "test2"
        pwd = "maverick1a"
        name = "shah"
        email = "abc@ymail.com"
        msg = "I need 10 spoons to rent, do you have 10 spoons available? Please let me know."

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
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[7]/div/div/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[4]/a[1]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/form/input[2]").clear()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/input[2]")
        elem.send_keys(name)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/form/input[3]").clear()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/input[3]")
        elem.send_keys(email)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/form/textarea").clear()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/textarea")
        elem.send_keys(msg)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/input[4]").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Contacted owner successfully"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
