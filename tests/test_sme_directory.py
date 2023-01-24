import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.reports.sme_directory_page import SMEDirectory

class TestSmeDirectory(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)    

    def test_sme_directory(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(8)                     
        login.login_btn()
        self.driver.get("https://demo.dcareug.com/uiatest/Reports/SMEDirectory")
        sme_directory = SMEDirectory(self.driver)
        sme_directory.export_btn()
        self.assertEquals("SME Directory - UIA SME Portal", self.driver.title)
   
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()