import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.support_organisations.pending_support_org_page import PendingSupportOrg

class TestPendingSupportOrg(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_pending_support_organisation(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(15)                     
        login.login_btn()
        self.driver.get('https://demo.dcareug.com/uiatest/BusinessSupportOrg/PendingOrganisation')
        time.sleep(5)
        pend_support_org = PendingSupportOrg(self.driver)
        pend_support_org.enter_region('Central')
        time.sleep(3)
        pend_support_org.enter_subregion('Central')
        time.sleep(3)
        pend_support_org.enter_district('Buikwe')
        time.sleep(3)
        pend_support_org.enter_page_size('20')
        time.sleep(3)
        pend_support_org.filter_data_btn()
        self.assertEquals("Business Support Organisation - UIA SME Portal", self.driver.title)
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()