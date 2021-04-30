import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_signup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        username = "test2"
        firstname = "Test2"
        lastname = "SignUp2"
        email = "t2@yahoo.com"
        phone = "1234567890"
        pwd = "maverick1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/form/a[2]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username)
        time.sleep(1)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        time.sleep(1)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(firstname)
        time.sleep(1)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(lastname)
        time.sleep(1)
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys(phone)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys(pwd)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(pwd)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        assert "Signed Up and Logged In"
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
