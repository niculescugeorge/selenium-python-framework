import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _all_courses_btn = "//div[@id='navbar-inverse-collapse']//a[@href='/courses']"
    _search_box = "//input[@id='search']"
    _search_btn = "//button[contains(@class, 'search-course')]"
    _course = "//h4[contains(@class, 'dynamic-heading') and contains(text(), '{0}')]"
    _enroll_button = "//button[text() = 'Enroll in Course']"
    _cc_num = "//input[@aria-label = 'Credit or debit card number']"
    _cc_exp_date = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _buy_btn = "//button[contains(@class, 'checkout-button')][1]"
    _enroll_error_message = "//span[contains(text(), 'Your card number is incomplete.')]"

    ############################
    ### Element Interactions ###
    ############################

    def click_all_courses_btn(self):
        self.element_click(self._all_courses_btn, locator_type="xpath")

    def enter_course_name(self, name):
        self.sendKeys(name, locator=self._search_box, locator_type="xpath")
        self.click_search_btn()

    def click_search_btn(self):
        self.element_click(self._search_btn, locator_type="xpath")

    def select_course_to_enroll(self, full_course_name):
        self.element_click(locator=self._course.format(full_course_name), locator_type="xpath")

    def click_on_enroll_btn(self):
        self.element_click(self._enroll_button, locator_type="xpath")

    def enter_card_number(self, num):
        self.switchToFrame(index=0)
        self.sendKeys(num, locator=self._cc_num, locator_type="xpath")
        self.switchToDefaultContent()

    def enter_card_exp_date(self, exp_date):
        self.SwitchFrameByIndex(self._cc_exp_date, locatorType="xpath")
        self.sendKeys(exp_date, locator=self._cc_exp_date, locator_type="xpath")
        self.switchToDefaultContent()

    def enter_card_cvv(self, cc_cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cc_cvv, locator=self._cc_cvv, locator_type="xpath")
        self.switchToDefaultContent()

    def click_buy_btn(self):
        self.element_click(locator=self._buy_btn, locator_type="xpath")

    def enter_credit_card_information(self, num, exp_date, cc_cvv):
        self.enter_card_number(num)
        self.enter_card_exp_date(exp_date)
        self.enter_card_cvv(cc_cvv)

    def enrollCourse(self, num="", exp_date="", cc_cvv=""):
        self.click_on_enroll_btn()
        self.webScroll(direction="down")
        self.enter_credit_card_information(num, exp_date, cc_cvv)
        self.click_buy_btn()

    def verifyEnrollFailed(self):
        message_element = self.wait_for_element(self._enroll_error_message, locator_type="xpath")
        result = self.isElementDisplayed(element=message_element, locatorType="xpath")
        return result








