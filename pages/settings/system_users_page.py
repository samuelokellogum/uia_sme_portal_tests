from selenium.webdriver.common.by import By

class SystemUser:

    def __init__(self, driver):
        self.driver = driver    

    def click_next_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='2']").click()   

    def click_next_next_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='3']").click()        
