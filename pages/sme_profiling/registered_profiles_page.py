from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegisteredProfile:
    # SME Status
    dashboard_button_xpath = "//button[normalize-space()='DASHBOARD']"
    add_sme_profile_btn = "//a[normalize-space()='Add SME Profile']"    
    next_btn =  "//input[@class='next action-button pull-right valid']"    
    #next_btn = "//body/div/main[@role='main']/form[@id='msform']/div/div/div/div/div/div/fieldset[1]/input[1]"
    select_region = "RegionId"
    select_subregion = "SubRegionId"
    select_district = "DistrictId"
    select_county = "CountyId"
    select_subcounty = "SubCountyId"
    select_parish = "ParishId"
    select_gender = "GenderId"
    select_education_level = "EducationLevelId"
    select_marital_status = "MaritalStatusId"
    select_msme_premises = "MSMEPremissesId"
    select_how_business_started = "HowBusinessStartedId"
    select_biz_decision_making = "BusinessDecisionMakingId"
    select_ownership_structure = "OwnershipStructureId"
    select_uia_entity = "//input[@id='RegistrationEntities"
    select_ursb_entity = "//input[@id='RegistrationEntities"
    select_local_government = "//input[@id='RegistrationEntities"
    # SME Statistics
    select_total_assets_previous = "//input[@id='TotalAsset']"
    select_total_assets_current = "//input[@id='CurrentYearTotalAsset']"
    select_total_assets_next = "//input[@id='NextYearTotalAsset']"
    select_annual_turnover_previous = "//input[@id='AnnualTurnOvers']"
    select_annual_turnover_current = "//input[@id='CurrentYearAnnualTurnOvers']"
    select_annual_turnover_next = "//input[@id='NextYearAnnualTurnOvers']"
    select_year_biz_started_id = "LengthOfMSMEinOperation"
    select_msme_sector_id = "MSMESectorId" # Agriculture, forestry and fishing
    select_sub_sector_id = "MSMESubSectorId" # Forestry and logging
    select_group_id = "MSMEGroupId" # Logging
    select_class_id = "MSMEClassId" # Logging
    select_main_value_chain = "MainValueChainId"
    select_main_role_value_chain = "MainRoleValueChainId"
    main_needs_access_market_1 = "//button[@title='1']//div//div//div"
    main_needs_access_market_2 = "//button[@title='2']//div//div//div"
    main_needs_access_market_3 = "//button[@title='3']//div//div//div"
    link_add_product_buyer = "//a[normalize-space()='Add Product Buyer']"
    add_buyer_id = "ProductBuyers[0].ProductServiceBuyerId" #Exporters
    select_production_capacity = "ProductionCapacityId" # 11-20
    select_member_of_appex_org_id = "MemberOfApexOrganisationId" # No
    select_biz_linkages_id = "keylinkagesId" # Key Customers
    select_if_engaged_cross_border_trade_id = "EngagedInCrossBorderTradeId" # No    
    select_next_step_btn = "//input[@class='next action-button pull-right valid']"
    # SME Economic Environment
    select_financial_source_id = "FinancingSourceDetails" # Cooperatives
    select_funding_option_id = "FundingOptionId" # Debt financing
    select_info_details_id = "InformationSourceDetails" # Government
    select_use_of_tech_status_id = "SMEUseAnyTeachnologyId" # No
    select_msme_building_needs = "//div[@id='CapacityBuildingDiv']//table//tfoot//tr//td//a"
    save_button = "//input[@id='saveButton']"
        
    # Initialise the driver
    def __init__(self, driver):
        self.driver = driver

    def click_add_sme_profile_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Add SME Profile']").click()

    def enter_region(self, region):        
        drop = Select(self.driver.find_element(By.ID, self.select_region))
        drop.select_by_visible_text(region)        

    def enter_subregion(self, subregion):        
        drop = Select(self.driver.find_element(By.ID, self.select_subregion))
        drop.select_by_visible_text(subregion)        

    def enter_district(self, district):        
        drop = Select(self.driver.find_element(By.ID, self.select_district))
        drop.select_by_visible_text(district)        

    def enter_county(self, county):        
        drop = Select(self.driver.find_element(By.ID, self.select_county))
        drop.select_by_visible_text(county)        

    def enter_subcounty(self, subcounty):        
        drop = Select(self.driver.find_element(By.ID, self.select_subcounty))
        drop.select_by_visible_text(subcounty)        

    def enter_parish(self, parish):        
        drop = Select(self.driver.find_element(By.ID, self.select_parish))
        drop.select_by_visible_text(parish)        

    def enter_village(self, village):        
        self.driver.find_element(By.XPATH, "//input[@id='Villages']").send_keys(village)        

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(firstname)    

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lastname)  

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
        drop = Select(self.driver.find_element(By.ID, self.select_education_level))
        drop.select_by_visible_text(educ_level)      

    def enter_gender(self, gender):        
        drop = Select(self.driver.find_element(By.ID, self.select_gender))
        drop.select_by_visible_text(gender)      

    def enter_sme_premises(self, premises):        
        drop = Select(self.driver.find_element(By.ID, self.select_msme_premises))
        drop.select_by_visible_text(premises)

    def enter_businessname(self, businessname):  
        self.driver.find_element(By.XPATH, "//input[@id='BusinessName']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='BusinessName']").send_keys(businessname)         

    def enter_other_registration_entity(self, otherentity):  
        self.driver.find_element(By.XPATH, "//input[@id='OtherRegistrationEntity']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='OtherRegistrationEntity']").send_keys(otherentity)         

    def enter_how_business_started(self, business):        
        drop = Select(self.driver.find_element(By.ID, self.select_how_business_started))
        drop.select_by_visible_text(business)
              
    def enter_male_employees(self, male):  
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesMale']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesMale']").send_keys(male)

    def enter_female_employees(self, female):  
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesFemale']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='EmployeesFemale']").send_keys(female)
    
    def enter_biz_decision_making(self, decision):        
        drop = Select(self.driver.find_element(By.ID, self.select_biz_decision_making))
        drop.select_by_visible_text(decision)

    def enter_owner_structure(self, structure):        
        drop = Select(self.driver.find_element(By.ID, self.select_ownership_structure))
        drop.select_by_visible_text(structure)
              
    def first_create_sme_profile(self):
        self.driver.find_element(By.XPATH, "//input[@class='next action-button pull-right valid']").click()

    def select_next_step_btn(self):
        self.driver.find_element(By.XPATH, self.select_next_step_btn).click()

    def select_total_assets_previous(self, previous):
        self.driver.find_element(By.XPATH, self.select_total_assets_previous).send_keys(previous)

    def select_total_assets_current(self, current):
        self.driver.find_element(By.XPATH, self.select_total_assets_current).send_keys(current)

    def select_total_assets_next(self, next):
        self.driver.find_element(By.XPATH, self.select_total_assets_next).send_keys(next)

    def select_annual_turnover_previous(self, previous):
        self.driver.find_element(By.XPATH, self.select_annual_turnover_previous).send_keys(previous)
    
    def select_annual_turnover_current(self, current):
        self.driver.find_element(By.XPATH, self.select_annual_turnover_current).send_keys(current)
    
    def select_annual_turnover_next(self, next):
        self.driver.find_element(By.XPATH, self.select_annual_turnover_next).send_keys(next)
    
    def select_year_biz_started(self, biz):
        drop = Select(self.driver.find_element(By.ID, self.select_year_biz_started_id))
        drop.select_by_visible_text(biz)
         
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    def save_btn(self):
        self.driver.find_element(By.XPATH, self.save_button).click()

    