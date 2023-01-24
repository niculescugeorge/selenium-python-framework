import time

from selenium.webdriver.common.by import By
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData(r"C:\Users\George\workspace_python\letskodeit\testdata.csv"))
    @unpack
    def test_invalidCourseBuy(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.click_all_courses_btn()
        self.courses.enter_course_name(courseName)
        time.sleep(1)
        self.courses.select_course_to_enroll(courseName)
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp_date=ccExp, cc_cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidCourseBuy", result, "Wrong information of credit card")

