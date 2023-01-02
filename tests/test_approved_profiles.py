import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.sme_profiling.approved_profiles_page import ApprovedProfile

class TestApprovedProfile(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_approved_sme_profiles(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(15)                     
        login.login_btn()
        self.driver.get('https://demo.dcareug.com/uiatest/Profile/AprovedProfiles')
        time.sleep(5)
        approved_profile = ApprovedProfile(self.driver)
        approved_profile.click_export_btn()
        time.sleep(15)        
      
    def test_display_only_approved_smes(self):
        approved_profile = ApprovedProfile(self.driver)   
        approved_profile.click_next_page()
        time.sleep(5)
        approved_profile.click_next_next_page()
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()