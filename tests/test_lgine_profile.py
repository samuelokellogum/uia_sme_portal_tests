import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.sme_profiling import *

class TestLgineProfile(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_access_lgine_profile_page(self):  
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")
        time.sleep(7)
        login.login_btn()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uiatest/Logine/Questionnaire")         
       
    def add_sme_profile(self):
        self.driver.get("https://demo.dcareug.com/uiatest/Profile/Update")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()