import time
import unittest
from selenium import webdriver
from uia_sme_portal_tests.pages.login_page import Login
from uia_sme_portal_tests.pages.sme_profiling.registered_profiles_page import RegisteredProfile

class TestSMEProfile(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # def test_sme_profile(self):  
    #     pass
   
    def test_add_sme_profile(self):
        login = Login(self.driver)        
        login.enter_username("admin")
        login.enter_password("administrator")
        time.sleep(15)
        login.login_btn()
        # self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uiatest/Profile/RegisteredProfiles")
        register = RegisteredProfile(self.driver)
        register.click_add_sme_profile_btn()
        register.enter_region('Central')
        #register.enter_subregion('Central')
        #register.enter_district('BUIKWE')
        #register.enter_county('BUIKWE COUNTY SOUTH')
        time.sleep(20)
        #register.enter_subcounty('BUIKWE')
        #register.enter_parish('KITAZI')
        register.enter_village('Buikwe Village 1')
        register.enter_firstname('Samuel')
        register.enter_lastname('Okello')
        register.enter_othername('Elijah')
        register.enter_dob('1990-06-12')
        register.enter_email('test@test.com')
        register.enter_phonenumber('(256) 778-571054')
        register.enter_education_level('Primary')
        register.enter_gender('Male')
        register.enter_sme_premises('Rented')
        register.enter_businessname('Test Company')
        register.enter_other_registration_entity('Other Test Name')
        register.enter_how_business_started('With a partner')
        register.enter_male_employees('6')
        register.enter_female_employees('5')
        register.enter_biz_decision_making('Individual')
        register.enter_owner_structure('Partnership')
        #register.first_create_sme_profile()   
        time.sleep(5)
        # register.select_next_step_btn()
        # register.select_year_biz_started('2021')
        # time.sleep(15)
        register.save_btn()
        self.driver.implicitly_wait(15)     
   
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()