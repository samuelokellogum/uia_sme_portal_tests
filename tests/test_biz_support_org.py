import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.support_organisations.business_support_org_page import BusinessSupportOrg


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
        time.sleep(3)
        biz_support_org.enter_subregion('Central')
        time.sleep(3)
        biz_support_org.enter_district('Buikwe')
        biz_support_org.enter_no_of_male_employees('14')
        biz_support_org.enter_no_of_female_employees('23')
        biz_support_org.enter_telephone('0778676543')
        biz_support_org.enter_contact_person('Chief Executive Officer')
        biz_support_org.enter_po_box('P.O.Box 2345')
        biz_support_org.enter_fax('567')
        biz_support_org.enter_email('admin@admin.com')
        biz_support_org.enter_website('www.sample.com')
        biz_support_org.enter_title('CEO')
        time.sleep(30)    
        biz_support_org.save_btn()
        self.assertEquals("Business Support Organisation - UIA SME Portal", self.driver.title)
       
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()