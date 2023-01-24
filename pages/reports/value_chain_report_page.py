from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ValueChainReport:

    def __init__(self, driver):
        self.driver = driver               

    def export_report_btn(self):
        self.driver.find_element(By.XPATH, "//b[normalize-space()='Export']").click()
    