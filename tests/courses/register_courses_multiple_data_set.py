import time

from selenium.webdriver.common.by import By
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "10/27", "444"),
          ("Learn Python 3 from scratch", "20", "1220", "20"))
    @unpack
    def test_invalidCourseBuy(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.click_all_courses_btn()
        self.courses.enter_course_name(courseName)
        self.courses.select_course_to_enroll(courseName)
        time.sleep(3)
        self.courses.enrollCourse(num=ccNum, exp_date=ccExp, cc_cvv=ccCVV)
        time.sleep(5)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidCourseBuy", result, "Wrong information of credit card")
        self.driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
