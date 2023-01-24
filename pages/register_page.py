from selenium.webdriver.common.by import By

class Register:    

    def __init__(self, driver):
        self.driver = driver     

    def navigate_register_page(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

    def enter_firstname(self, username):  
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(username)        

    def enter_lastname(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(password)

    def enter_phonenumber(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='PhoneNumber']").send_keys(code)

    def enter_email(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='UserEmail']").send_keys(code)

    def enter_password(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(code)

    def enter_confirm_password(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys(code)
    
    def save_btn(self):
        self.driver.find_element(By.XPATH, "//input[@id='saveButton']").click()
