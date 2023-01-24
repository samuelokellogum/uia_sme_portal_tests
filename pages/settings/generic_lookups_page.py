from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class GenericLookup:
    lookup_category_dropdown_id = "LookupType" # Energy Source Challenge
    look_up_btn = "//a[normalize-space()='Add Lookup']"

    def __init__(self, driver):
        self.driver = driver   
        
    def enter_lookup_category(self, category):
        drop = Select(self.driver.find_element(By.ID, self.lookup_category_dropdown_id))
        drop.select_by_visible_text(category)        

    def lookup_btn(self):
        self.driver.find_element(By.XPATH, self.look_up_btn).click()

    def lookup_class_mappings_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Lookup Class Mappings']").click()            

    def enter_code(self, code):
        self.driver.find_element(By.XPATH, "//input[@id='Code']").send_keys(code)

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(name)

    def enter_description(self, description):
        self.driver.find_element(By.XPATH, "//input[@id='Description']").send_keys(description)

    def save_and_continue(self):
        self.driver.find_element(By.XPATH, "//input[@value='Save & Continue']").click()

        
