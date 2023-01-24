import time

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("niculescu.georgerobert@yahoo.com", "letskodeit")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyLoginSuccesful()
        self.ts.markFinal("test_validLogin", result2, "Login was succesful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        time.sleep(7)
        result = self.lp.verifyLoginFailed()
        assert result == True






