from selenium.webdriver.common.by import By

class Signup:    
        
    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lastname)

    def enter_telephone(self, tel):
        self.driver.find_element(By.XPATH, "//input[@id='PhoneNumber']").send_keys(tel)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='UserEmail']").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)

    def enter_confirm_password(self, confirmpassword):
        self.driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys(confirmpassword)

    def enter_security_code(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='DNT_CaptchaInputText']").send_keys(code)
    
    def save_btn(self):
        self.driver.find_element(By.XPATH, "//input[@id='saveButton']").click()

    