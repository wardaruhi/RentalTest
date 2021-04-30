import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class rent_start(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "instructor"
        pwd = "gounomavs1a"
        startdate = "05/01/2021"
        name = "Jerry"
        phone = "1234567895"

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
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[4]/h4/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[3]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        obj = Select(driver.find_element_by_name("item"))
        obj.select_by_index(1)
        time.sleep(1)
        elem = driver.find_element_by_id("id_rentStartDate")
        elem.send_keys(startdate)
        time.sleep(1)
        elem = driver.find_element_by_id("id_renterName")
        elem.send_keys(name)
        time.sleep(1)
        elem = driver.find_element_by_id("id_renterPhoneNumber")
        elem.send_keys(phone)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Rent started successfully"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
