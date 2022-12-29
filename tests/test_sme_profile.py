import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.sme_profiling.registered_profiles_page import RegisteredProfile

class TestSMEProfile(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uia/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # def test_smeprofile(self):  
    #     login = Login(self.driver)
    #     login.enter_username("admin")
    #     login.enter_password("administrator")
    #     login.click_login()
    #     self.driver.implicitly_wait(5)
    #     self.driver.get("https://demo.dcareug.com/uiatest/")
    #     self.assertEquals('SME Profile - UIA', self.driver.title)

    def test_registered_profile(self):
        login = Login(self.driver)
        register = RegisteredProfile(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")
        login.click_login()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uiatest/Profile/RegisteredProfiles")
        register.click_add_sme_profile_btn()
        register.enter_region()
        register.enter_subregion()
        register.enter_district()
        register.enter_county()
        register.enter_subcounty()
        register.enter_parish()
        register.enter_village()
        register.enter_firstname()
        register.enter_lastname()
        register.enter_othername()
        register.enter_dob('1990-06-12')
        register.enter_email('test@test.com')
        register.enter_phonenumber('+256778766543')
        register.enter_education_level()
        register.enter_gender()
        register.enter_sme_premises()
        register.enter_businessname()
        register.enter_other_registration_entity()
        register.enter_how_business_started()
        register.enter_male_employees()
        register.enter_female_employees()
        register.enter_biz_decision_making()
        register.enter_owner_structure()
        register.first_create_sme_profile()   
        self.driver.implicitly_wait(15)     

    # def test_logout(self):
    #     self.assert_(False)  

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main()