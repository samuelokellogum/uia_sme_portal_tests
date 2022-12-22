import time
import unittest
from selenium import webdriver
import sys

# Import Pages Needed for the tests
from uia_sme_portal_tests.pages.register_page import Register

class TestRegister(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_register(self):  
        register = Register(self.driver)
        # self.driver.get('https://demo.dcareug.com/uiatest/Account/UserRegister')
        #https://demo.dcareug.com/uiatest/Index
        register.navigate_register_page()
        register.enter_firstname('sam')
        register.enter_lastname('samu')
        register.enter_phonenumber('0789899098')
        register.enter_email('sam@sam.com')
        register.enter_password('1Q2w3e4r5t@')
        register.enter_confirm_password('1Q2w3e4r5t@')
        time.sleep(15)          
        register.save_btn()
        self.assert_(True)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()