from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """This class is the parent of all pages"""
    """It contains all the generic automation methods such as clicking, getting, entering text"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def do_enter(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.ENTER)

    # this creates a list of elements and choose the first one
    def multiple_elements(self, by_locator, index_number):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located(by_locator))
        element[index_number].click()

    def clear_input_field(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_dropdown_menu(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        drp = Select(element)
        drp.select_by_visible_text(text)
