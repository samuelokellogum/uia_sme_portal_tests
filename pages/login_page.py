from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver           

    def enter_username(self, username):  
        self.driver.find_element(By.XPATH, "//input[@id='UsernameOrEmail']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='UsernameOrEmail']").send_keys(username)        

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)

    def enter_security_code(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='DNT_CaptchaInputText']").send_keys(code)

    def login_btn(self):
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()


    
