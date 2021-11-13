import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


# Settings > Tools > Python Integrated Tools > Default test runner is set to pytest

class Test_HomePage(BaseTest):

    def test_signup_link_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_signup_link_exist()
        assert flag

    def test_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_title(TestData.home_page_title)
        assert title == TestData.home_page_title

    def test_sign_in(self):
        self.homePage = HomePage(self.driver)
        self.homePage.sign_in()

    def test_search_box_working(self):
        self.homepage = HomePage(self.driver)
        self.homepage.search_box_working()

    def test_choose_item_from_homepage(self):
        self.homepage = HomePage(self.driver)
        self.homepage.choose_item_from_homepage()

    def test_buy_item_from_homepage(self):
        self.homepage = HomePage(self.driver)
        self.homepage.buy_item_from_homepage()
