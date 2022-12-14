import unittest
from selenium import webdriver
import sys

# Import Pages Needed for the tests
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.smeprofiling import *

class TestSettings(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uia/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_access_lgineprofilepage(self):  
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")
        login.click_login()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uiatest/Logine/Questionnaire")         
        self.assertEquals('LGINE Profiles - UIA SME Portal', self.driver.title)

    def add_sme_profile(self):
        self.driver.get("https://demo.dcareug.com/uiatest/Profile/Update")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.assertEquals('Sme Profile - UIA SME Portal', self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()