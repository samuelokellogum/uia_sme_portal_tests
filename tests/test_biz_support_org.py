import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.support_organisations.approved_support_org_page import ApprovedSupportOrg
from uia_sme_portal_tests.pages.support_organisations.business_support_org_page import BusinessSupportOrg
from uia_sme_portal_tests.pages.support_organisations.pending_support_org_page import PendingSupportOrg

class TestBizSupportOrg(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_biz_support_organisation(self):
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")                
        time.sleep(15)                     
        login.login_btn()
        self.driver.get('https://demo.dcareug.com/uiatest/BusinessSupportOrg/Index')
        time.sleep(5)
        biz_support_org = BusinessSupportOrg(self.driver)
        biz_support_org.add_new_org_btn()
        biz_support_org.enter_region('Central')
        biz_support_org.enter_subregion('Central')
        biz_support_org.enter_district('Buikwe')        
        time.sleep(30)    
        biz_support_org.save_btn()
        self.assertTrue(True)
        
      
    # def test_approved_support_organisation(self):
    #     login = Login(self.driver)
    #     login.enter_username("admin")
    #     login.enter_password("administrator")                
    #     time.sleep(15)                     
    #     login.login_btn()
    #     self.driver.get('https://demo.dcareug.com/uiatest/BusinessSupportOrg/ApprovedOrganisation')
    #     time.sleep(5)
    #     app_support_org = ApprovedSupportOrg(self.driver)
        

    # def test_pending_support_organisation(self):
    #     login = Login(self.driver)
    #     login.enter_username("admin")
    #     login.enter_password("administrator")                
    #     time.sleep(15)                     
    #     login.login_btn()
    #     self.driver.get('https://demo.dcareug.com/uiatest/BusinessSupportOrg/PendingOrganisation')
    #     time.sleep(5)
    #     pend_support_org = PendingSupportOrg(self.driver)
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()