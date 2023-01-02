import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.settings.system_users_page import SystemUser

class TestSettings(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_create_lookup(self):  
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")
        login.login_btn()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uia/Lookup/Details") 
 

    def test_system_users_activated_and_pending(self):
        self.driver.get("https://demo.dcareug.com/uiatest/Account/SystemUsers") 
        system_user = SystemUser(self.driver)
        # system_user.click_next_btn()        
        time.sleep(5)
        # system_user.click_next_next_btn()
        self.assertTrue(True)
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()