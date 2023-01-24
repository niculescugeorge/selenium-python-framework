import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import logging


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators

    _sign_in_btn = "//a[@href = '/login']"
    _email_field = "email"
    _password_field = "password"
    _login_btn = "//input[@value = 'Login']"

    def clickSignInBtn(self):
        self.element_click(self._sign_in_btn, locator_type="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginBtn(self):
        self.element_click(self._login_btn, locator_type="xpath")

    def login(self, email="", password=""):
        self.clickSignInBtn()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifyLoginSuccesful(self):
        result = self.isElementPresent("dropdownMenu1")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(), 'Your username or password is invalid. Please try again.')]",
                                         locator_type="xpath")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("Google")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.wait_for_element(locator="//a[@href='/logout']", locator_type="xpath", poll_frequency=1)
        self.element_click(element=logoutLinkElement)