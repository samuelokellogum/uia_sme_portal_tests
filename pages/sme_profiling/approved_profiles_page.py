from selenium.webdriver.common.by import By

class ApprovedProfile:

    def __init__(self, driver):
        self.driver = driver   

    def click_export_btn(self):
        self.driver.find_element(By.XPATH, "//main[@role='main']//p//a//b").click()    

    def click_next_page(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='2']").click()     

    def click_next_next_page(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='3']").click() 

    def click_last_page(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Last']").click()      

    def click_toggle_filter_btn(self):
        self.driver.find_element(By.XPATH, "//p//a[@role='button']").click()            

    