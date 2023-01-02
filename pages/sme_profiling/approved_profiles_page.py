from selenium.webdriver.common.by import By

class ApprovedProfile:

    def __init__(self, driver):
        self.driver = driver   

    def click_export_btn(self):
        self.driver.find_element(By.XPATH, "//main[@role='main']//p//a//b").click()            

    def click_toggle_filter_btn(self):
        self.driver.find_element(By.XPATH, "//p//a[@role='button']").click()            

    