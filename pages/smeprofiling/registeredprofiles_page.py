from selenium.webdriver.common.by import By


class RegisteredProfile:
    # Locators of all the elements    
    dashboard_button_xpath = "//button[normalize-space()='DASHBOARD']"
    add_sme_profile_btn = "//a[normalize-space()='Add SME Profile']"
    next_btn = "//input[@class='next action-button pull-right valid']"
    select_region = "//span[normalize-space()='Central']"
    
    # Initialise the driver
    def __init__(self, driver):
        self.driver = driver


    def click_add_sme_profile_btn(self):
        self.driver.find_element_by_xpath(By.XPATH, "//a[normalize-space()='Add SME Profile']").click()

    def enter_region(self, region):
        region_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.region_dropdown_id))
        drop.select_by_visible_text(region)        

    def enter_subregion(self, region):
        subregion_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.subregion_dropdown_id))
        drop.select_by_visible_text(region)        

    def enter_district(self, district):
        district_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.district_dropdown_id))
        drop.select_by_visible_text(district)        

    def enter_county(self, county):
        county_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.county_dropdown_id))
        drop.select_by_visible_text(county)        

    def enter_subcounty(self, subcounty):
        subcounty_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.subcounty_dropdown_id))
        drop.select_by_visible_text(subcounty)        

    def first_create_sme_profile(self):
        self.driver.find_element(By.PATH, self.next_btn).click()

    # Action method for every element
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    