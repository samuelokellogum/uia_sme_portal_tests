import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.reports.data_dump_page import DataDump

class TestDataDumps(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)    
    
    def test_data_dumps(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(8)                     
        login.login_btn()
        self.driver.get("https://demo.dcareug.com/uiatest/Profile/DataDumps")
        data_dump = DataDump(self.driver)
        data_dump.generate_data_dump_btn()
        time.sleep(5)
        data_dump.download_link()
        self.assertEquals("Dump - UIA SME Portal", self.driver.title)
   
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()