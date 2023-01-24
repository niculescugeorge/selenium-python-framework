from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from base.basepage import BasePage
import logging


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _home = "HOME"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _sign_in_btn = "//a[@href = '/login']"
    _user_icon = "//button[@id='dropdownMenu1']"

    def navigateToHome(self):
        self.element_click(self._home, locator_type="link")

    def navigateToAllCourses(self):
        self.element_click(self._all_courses, locator_type="link")

    def navigateToSupport(self):
        self.element_click(self._support, locator_type="link")

    def navigateToSignIn(self):
        self.element_click(self._sign_in_btn, locator_type="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.wait_for_element(self._user_icon, locator_type="id", poll_frequency=1)
        self.element_click(element=userSettingsElement)

