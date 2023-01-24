from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BusinessSupportOrg:
    
    def __init__(self, driver):
        self.driver = driver    

    def enter_region(self, region):     
        region_dropdown_id = ""
        drop = Select(self.driver.find_element(By.ID, self.region_dropdown_id))
        drop.select_by_visible_text(region)        

    def enter_subregion(self, subregion):          
        subregion_dropdown_id = ""
        drop = Select(self.driver.find_element(By.ID, self.subregion_dropdown_id))
        drop.select_by_visible_text(subregion)        

    def add_new_org_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='New Organisation']").click()   

    def enter_name_of_company(self, company):
        self.driver.find_element(By.XPATH, "//input[@id='OrganisationName']").send_keys(company)

    def enter_street_address(self, street):
        self.driver.find_element(By.XPATH, "//input[@id='StreetAddress']").send_keys(street)

    def save_btn(self):
        self.driver.find_element(By.XPATH, "//input[@value='Save']").click()

    


