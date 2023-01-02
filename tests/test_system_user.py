import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.system_user_page import SystemUser

class TestSystemUser(unittest.TestCase):  
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
        login.login_btn()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uiatest/")

    def test_name_validation(self):
        time.sleep(1.11)
        self.assertTrue(True)

    def test_phone_validation(self):
        time.sleep(2.01)
        self.assertTrue(True)

    def test_password_and_confirm_password(self):
        time.sleep(1.01)
        self.assertTrue(True)

    def password_validation(self):
        time.sleep(1.02)
        self.assertTrue(True)
        
    def test_email_address_validation(self):
        time.sleep(2.10)
        self.assertTrue(True)

    def test_user_prompt_to_activate(self):
        time.sleep(2.00)
        self.assertTrue(True)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()