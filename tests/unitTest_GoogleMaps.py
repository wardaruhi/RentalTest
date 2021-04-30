import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class rent_gmaps(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rent(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://rentapp-assignment5.herokuapp.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/a/img").click()
        time.sleep(10)
        assert "Google Map works successfully"

        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
