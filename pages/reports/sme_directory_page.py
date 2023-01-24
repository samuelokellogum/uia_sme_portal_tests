from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SMEDirectory:

    def __init__(self, driver):
        self.driver = driver     

    def export_btn(self):
        self.driver.find_element(By.XPATH, "//b[normalize-space()='Export']").click()          

    