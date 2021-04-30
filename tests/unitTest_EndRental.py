import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_end(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "instructor"
        pwd = "gounomavs1a"
        enddate = "05/07/2021"
        notes = "Thank you, great product, price and customer service"

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
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[3]/td[7]/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_rentEndDate")
        elem.send_keys(enddate)
        time.sleep(1)
        elem = driver.find_element_by_id("id_notes")
        elem.send_keys(notes)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Rent ended successfully"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
