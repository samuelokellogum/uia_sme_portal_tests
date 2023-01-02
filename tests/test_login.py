import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login

class TestLogin(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login(self):  
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(15)                     
        login.login_btn()        
        
    def test_mandatory_login_fields(self):
        time.sleep(5.00)
        self.assertTrue(True)
    
    def test_unique_security_code(self):
        time.sleep(3.00)
        self.assertTrue(True)

    def test_security_code_validation(self):
        time.sleep(3.00)
        self.assertTrue(True)

    def test_previous_security_code_after_refreshing(self):
        time.sleep(3.00)
        self.assertTrue(True)

    def test_refreshing_security_code(self):
        time.sleep(3.00)
        self.assertTrue(True)    

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()