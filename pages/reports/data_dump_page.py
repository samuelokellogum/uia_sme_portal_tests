from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DataDump:

    def __init__(self, driver):
        self.driver = driver      

    def generate_data_dump_btn(self):
        self.driver.find_element(By.XPATH, "//b[normalize-space()='Generate Data Dump']").click()         

    def download_link(self):
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/main[1]/div[1]/table[1]/tbody[1]/tr[1]/th[2]/div[1]/a[1]/b[1]").click()

    