from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ApprovedSupportOrg:
    pagesize_dropdown_id = "Filters_PageSize"
    region_dropdown_id = "Filters_Enc_RegionId"
    subregion_dropdown_id = "Filters_Enc_SubRegionId"
    district_dropdown_id = "Filters_Enc_DistrictId"

    def __init__(self, driver):
        self.driver = driver               

    def enter_region(self, region):    
        drop = Select(self.driver.find_element(By.ID, self.region_dropdown_id))
        drop.select_by_visible_text(region)        

    def enter_subregion(self, subregion):
        drop = Select(self.driver.find_element(By.ID, self.subregion_dropdown_id))
        drop.select_by_visible_text(subregion)        

    def enter_district(self, district):
        drop = Select(self.driver.find_element(By.ID, self.district_dropdown_id))
        drop.select_by_visible_text(district)        

    def enter_page_size(self, pagesize):
        drop = Select(self.driver.find_element(By.ID, self.pagesize_dropdown_id))
        drop.select_by_visible_text(pagesize)     

    def filter_data_btn(self):
        self.driver.find_element(By.XPATH, "//input[@value='Filter Data']").click()  

    def clear_filter_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Clear Filters']").click() 