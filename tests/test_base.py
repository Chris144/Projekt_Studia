import unittest

from selenium import webdriver
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.driver.implicitly_wait(5)
        self.home_page = HomePage(self.driver)

    def test_checking_hoover_on_account(self):
        self.home_page = HomePage(self.driver)
        self.home_page.hoover_on_account()
        self.home_page.screenshot()

    def tearDown(self):
        self.driver.quit()
