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

    def enter_subregion(self, subregion):
        subregion_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.subregion_dropdown_id))
        drop.select_by_visible_text(subregion)        

    def enter_district(self, district):
        district_dropdown_id = "BUIKWE"
        drop = Select(self.driver.find_element(By.ID, self.district_dropdown_id))
        drop.select_by_visible_text(district)        

    def enter_county(self, county):
        county_dropdown_id = "BUIKWE COUNTY SOUTH"
        drop = Select(self.driver.find_element(By.ID, self.county_dropdown_id))
        drop.select_by_visible_text(county)        

    def enter_subcounty(self, subcounty):
        subcounty_dropdown_id = "BUIKWE"
        drop = Select(self.driver.find_element(By.ID, self.subcounty_dropdown_id))
        drop.select_by_visible_text(subcounty)        

    def enter_parish(self, parish):
        parish_dropdown_id = "KITAZI"
        drop = Select(self.driver.find_element(By.ID, self.parish_dropdown_id))
        drop.select_by_visible_text(parish)        

    def enter_village(self, village):
        village_dropdown_id = "Central"
        drop = Select(self.driver.find_element(By.ID, self.village_dropdown_id))
        drop.select_by_visible_text(village)    

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, "//input[@id='FirstName']").send_keys(firstname)    

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, "//input[@id='LastName']").send_keys(lastname)  

    def enter_othername(self, othername):  
        self.driver.find_element(By.XPATH, "//input[@id='OtherName']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='OtherName']").send_keys(othername)        

    def enter_phonenumber(self, phonenumber):  
        self.driver.find_element(By.XPATH, "//input[@id='PhoneNumber']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='PhoneNumber']").send_keys(phonenumber)        
 
    def enter_email(self, email):  
        self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)

    def enter_dob(self, dob):  
        self.driver.find_element(By.XPATH, "//input[@id='Dob']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Dob']").send_keys(dob)  

    def enter_education_level(self, educ_level):
        educ_level_dropdown_id = "//div[contains(text(),'Primary')]"
        drop = Select(self.driver.find_element(By.XPATH, self.educ_level_dropdown_id))
        drop.select_by_visible_text(educ_level)      

    def enter_gender(self, gender):
        gender_dropdown_id = "//div[contains(text(),'Male')]"
        drop = Select(self.driver.find_element(By.XPATH, self.gender_dropdown_id))
        drop.select_by_visible_text(gender)      

    def enter_sme_premises(self, gender):
        sme_premises_dropdown_id = "//div[contains(text(),'Rented')]"
        drop = Select(self.driver.find_element(By.XPATH, self.sme_premises_dropdown_id))
        drop.select_by_visible_text(gender)

    def enter_businessname(self, businessname):  
        self.driver.find_element(By.XPATH, "//input[@id='BusinessName']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='BusinessName']").send_keys(businessname)         

    def enter_other_registration_entity(self, otherentity):  
        self.driver.find_element(By.XPATH, "//input[@id='OtherRegistrationEntity']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='OtherRegistrationEntity']").send_keys(otherentity)         

    def enter_how_business_started(self, gender):
        sme_premises_dropdown_id = "//div[contains(text(),'Rented')]"
        drop = Select(self.driver.find_element(By.XPATH, self.sme_premises_dropdown_id))
        drop.select_by_visible_text(gender)
              
    def enter_male_employees(self, male):  
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesMale']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesMale']").send_keys(male)

    def enter_female_employees(self, female):  
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesFemale']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesFemale']").send_keys(female)
    
    def enter_biz_decision_making(self, decision):
        decision_dropdown_id = "//div[contains(text(),'Individual')]"
        drop = Select(self.driver.find_element(By.XPATH, self.decision_dropdown_id))
        drop.select_by_visible_text(decision)

    def enter_owner_structure(self, structure):
        structure_dropdown_id = "//div[contains(text(),'Partnership')]"
        drop = Select(self.driver.find_element(By.XPATH, self.structure_dropdown_id))
        drop.select_by_visible_text(structure)
              
    def first_create_sme_profile(self):
        self.driver.find_element(By.PATH, self.next_btn).click()

    # Action method for every element
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    