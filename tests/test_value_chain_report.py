import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.reports.value_chain_report_page import ValueChainReport


class TestValueChainReport(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)        

    def test_value_chain_reports(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(10)                     
        login.login_btn()
        self.driver.get("https://demo.dcareug.com/uiatest/Reports/ValueChainReport")
        value_chain = ValueChainReport(self.driver)
        value_chain.export_report_btn()
        self.assertEquals("Value Chains Report - UIA SME Portal", self.driver.title)
      
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()