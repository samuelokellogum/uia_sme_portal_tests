import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.settings.generic_lookups_page import GenericLookup

class TestGenericLookup(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)    
    
    def test_update_lookup(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(8)                     
        login.login_btn()
        time.sleep(2)
        self.driver.get("https://demo.dcareug.com/uiatest/Lookups/Index")
        generic_lookup = GenericLookup(self.driver)
        generic_lookup.lookup_btn()
        generic_lookup.enter_lookup_category('Energy Source Challenge')
        generic_lookup.enter_code('356')
        generic_lookup.enter_name('Test Name')
        generic_lookup.enter_description('Test Description') 
        time.sleep(2)
        generic_lookup.save_and_continue()  
        self.assertEquals("Update Lookup - UIA SME Portal", self.driver.title)
   
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()