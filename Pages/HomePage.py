from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData


class HomePage(BasePage):
    """This is the child class of BasePage class. Using generic methods in the parent class,
    this call will perform website_specific actions"""

    # These are the locators:
    sign_up_link = (By.XPATH, '//a[@class="login"]')
    email_locator = (By.XPATH, '//input[@id="email"]')
    password_locator = (By.XPATH, '//input[@id="passwd"]')
    sign_in_button = (By.XPATH, '//button[@id="SubmitLogin"]')
    search_button = (By.XPATH, '//input[@id="search_query_top"]')
    clothes = (By.XPATH, '//a[@class="product_img_link"]')
    clothes_quantity = (By.XPATH, '//input[@id="quantity_wanted"]')
    size_dropdown_menu = (By.XPATH, '//select[@id="group_1"]')
    addtocart_button = (By.XPATH, '//button[@name="Submit"]')
    checkout_button = (By.XPATH, '//a[@title="Proceed to checkout"]')
    second_checkout_button = (By.XPATH, '//p//a[@title="Proceed to checkout"]')
    third_checkout_button = (By.XPATH, '//button[@name="processAddress"]')
    fourth_checkout_button = (By.XPATH, '//button[@name="processCarrier"]')
    terms_checkbox = (By.XPATH, '//div[@id="uniform-cgv"]')
    paybybankwire_button = (By.XPATH, '//a[@class="bankwire"]')
    confirm_order_button = (By.XPATH, '//button[@type="submit"]')

    # constructor of the HomePage class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    # These are the actions being automated in the website

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.sign_up_link)

    def sign_in(self):
        self.do_click(self.sign_up_link)
        self.do_send_keys(self.email_locator, TestData.email)
        self.do_send_keys(self.password_locator, TestData.password)
        self.do_click(self.sign_in_button)

    def search_box_working(self):
        self.do_send_keys(self.search_button, TestData.tshirt)
        self.do_enter(self.search_button)

    def choose_item_from_homepage(self):
        self.multiple_elements(self.clothes, 0)

    def buy_item_from_homepage(self):
        self.multiple_elements(self.clothes, 0)
        self.clear_input_field(self.clothes_quantity)
        self.do_send_keys(self.clothes_quantity, '2')
        self.do_dropdown_menu(self.size_dropdown_menu, TestData.size_shirt)
        self.do_click(self.addtocart_button)
        self.do_click(self.checkout_button)
        self.do_click(self.second_checkout_button)
        self.do_send_keys(self.email_locator, TestData.email)
        self.do_send_keys(self.password_locator, TestData.password)
        self.do_click(self.sign_in_button)
        self.do_click(self.third_checkout_button)
        self.do_click(self.terms_checkbox)
        self.do_click(self.fourth_checkout_button)
        self.do_click(self.paybybankwire_button)
        self.multiple_elements(self.confirm_order_button, 1)
