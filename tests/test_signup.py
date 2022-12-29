import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.signup_page import Signup

class TestSignup(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/UserRegister"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_signup(self):  
        signup = Signup(self.driver)
        signup.enter_firstname("sme")
        signup.enter_lastname("sme_1")
        signup.enter_telephone("0765453423")
        signup.enter_email("example@example.com")
        signup.enter_password("Administrator!123")
        signup.enter_confirm_password("Administrator!123")
        signup.enter_security_code("12345")
        signup.save_btn()        
        self.assertEquals('User Details - UIA SME Portal', self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()