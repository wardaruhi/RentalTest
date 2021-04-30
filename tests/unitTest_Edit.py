import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_edit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "test2"
        pwd = "maverick2a"
        itemDesc = "Good"

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
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[3]/h4/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[3]/p[1]/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div[4]/div/input").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_itemDescription")
        elem.send_keys(itemDesc)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[1]/h4/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        # elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[8]/div/div/a")
        # elem.send_keys(Keys.RETURN)
        # time.sleep(1)
        assert "Product edited successfully"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
