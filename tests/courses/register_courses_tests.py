import time

from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidCourseBuy(self):
        self.courses.click_all_courses_btn()
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_to_enroll("JavaScript for beginners")
        time.sleep(3)
        self.courses.enrollCourse(num="1234 5678 9012 3456", exp_date="10/27", cc_cvv="444")
        time.sleep(5)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidCourseBuy", result, "Wrong information of credit card")