import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class rent_add(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):
        user = "test2"
        pwd = "maverick2a"
        itemName = "Hand Shovel"
        itemCost = "5"

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
        elem = driver.find_element_by_id("addBtn")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("id_itemName")
        elem.send_keys(itemName)
        time.sleep(1)
        obj = Select(driver.find_element_by_name("category"))
        obj.select_by_index(2)
        time.sleep(1)
        elem = driver.find_element_by_id("id_costPerItem")
        elem.send_keys(itemCost)
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[8]/input[2]")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Product added successfully"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
