from selenium.webdriver.common.by import By
from selenium.webdriver.common.

class LGINEProfile:

    def __init__(self, driver):
        self.driver = driver               

    def enter_region(self, region):     
        region_dropdown_id = "//body[1]/div[1]/main[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/div[1]/div[1]/div[1]"
        drop = Select(self.driver.find_element(By.ID, self.region_dropdown_id))
        drop.select_by_visible_text(region)        

    def enter_subregion(self, subregion):          
        subregion_dropdown_id = "//body[1]/div[1]/main[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]/div[1]/div[1]/div[1]"
        drop = Select(self.driver.find_element(By.ID, self.subregion_dropdown_id))
        drop.select_by_visible_text(subregion)        

    def filter_data_btn(self):
        self.driver.find_element(By.XPATH, "//input[@value='Filter Data']").click()
