import time
import unittest
from selenium import webdriver
import sys

# Import Pages Needed for the tests
from uia_sme_portal_tests.pages.login_page import Login

class TestLogout(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_logout(self):  
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(15)                     
        login.login_btn()   
        time.sleep(5) 
        login.logout_btn()     
        self.assertEquals('Home - UIA SME Portal', self.driver.title)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()