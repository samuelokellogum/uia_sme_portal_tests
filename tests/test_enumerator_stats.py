import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.reports.data_dump_page import DataDump
from uia_sme_portal_tests.pages.reports.enumerator_stats_page import EnumeratorStat
from uia_sme_portal_tests.pages.reports.value_chain_report_page import ValueChainReport
from uia_sme_portal_tests.pages.reports.sme_directory_page import SMEDirectory

class TestEnumeratorStats(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)    
        
    def test_enumerator_stats(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(8)                     
        login.login_btn()
        self.driver.get("https://demo.dcareug.com/uiatest/Profile/EnumeratorStat")
        enumerator_stat = EnumeratorStat(self.driver)     
        time.sleep(12)
        enumerator_stat.enter_approval_status("Not Submitted")
        time.sleep(3)
        enumerator_stat.load_data_btn()
        time.sleep(7)
        enumerator_stat.export_btn()
        self.assertEquals("Enumerator Stats - UIA SME Portal", self.driver.title)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()