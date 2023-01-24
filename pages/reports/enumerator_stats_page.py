from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class EnumeratorStat:   
    start_date = "Filters_StartDate" 
    end_date = "Filters_EndDate" 
    approval_status_dropdown = "Filters_Status"

    def __init__(self, driver):
        self.driver = driver        

    def enter_start_date(self, start):
        self.driver.find_element(By.XPATH, self.start_date).send_keys(start)  

    def enter_end_date(self, end):
        self.driver.find_element(By.XPATH, self.end_date).send_keys(end)  

    def enter_approval_status(self, status):        
        drop = Select(self.driver.find_element(By.ID, self.approval_status_dropdown))
        drop.select_by_visible_text(status)    

    def load_data_btn(self):
        self.driver.find_element(By.XPATH, "//input[@value='Load Data']").click()   

    def export_btn(self):
        self.driver.find_element(By.XPATH, "//b[normalize-space()='Export']").click() 

    def logout_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
          

    