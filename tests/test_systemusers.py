import unittest
from selenium import webdriver

# Import Pages Needed for the tests
from uia_tests.pages.login_page import Login
from uia_tests.pages.systemuser_page import SystemUser

class TestSystemUser(unittest.TestCase):  
    driver = None
    baseURL = "https://demo.dcareug.com/uiatest/Account/Login"
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login(self):  
        login = Login(self.driver)
        login.enter_username("admin")
        login.enter_password("administrator")
        login.click_login()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.dcareug.com/uiatest/")
        self.assertEquals('System User - UIA', self.driver.title)

    def test_logout(self):
        self.assert_(False)  

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()