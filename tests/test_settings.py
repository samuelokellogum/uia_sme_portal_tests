import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login

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
        login.click_login()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uia/Lookup/Details") 
 
        self.assertEquals('New Lookup Value - MSD', self.driver.title)

    def test_edit_lookup(self):
        self.assert_(False)  

    def test_delete_lookup(self):
        self.assert_(False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()