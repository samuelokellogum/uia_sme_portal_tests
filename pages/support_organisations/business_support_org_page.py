from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BusinessSupportOrg:
    region_dropdown_id = "RegionId" 
    subregion_dropdown_id = "SubRegionId"
    district_dropdown_id = "DistrictId"
    year_dropdown_id = "YearEstablised"
    business_sector_id = "BusinessSectorId"
    business_sub_sector_id = "BusinessSubSectorId"
    
    def __init__(self, driver):
        self.driver = driver    

    def add_new_org_btn(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='New Organisation']").click()

    def enter_region(self, region):    
        drop = Select(self.driver.find_element(By.ID, self.region_dropdown_id))
        drop.select_by_visible_text(region)        

    def enter_subregion(self, subregion):
        drop = Select(self.driver.find_element(By.ID, self.subregion_dropdown_id))
        drop.select_by_visible_text(subregion)        

    def enter_district(self, district):
        drop = Select(self.driver.find_element(By.ID, self.district_dropdown_id))
        drop.select_by_visible_text(district)        

    def enter_telephone(self, telephone):
        self.driver.find_element(By.XPATH, "//input[@id='TelePhone']").send_keys(telephone)

    def enter_po_box(self, box):
        self.driver.find_element(By.XPATH, "//input[@id='PoBoxNumber']").send_keys(box)

    def enter_fax(self, fax):
        self.driver.find_element(By.XPATH, "//input[@id='Fax']").send_keys(fax)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)

    def enter_website(self, website):
        self.driver.find_element(By.XPATH, "//input[@id='Website']").send_keys(website)    

    def enter_year(self, year):
        drop = Select(self.driver.find_element(By.ID, self.year_dropdown_id))
        drop.select_by_visible_text(year)    

    def enter_no_of_male_employees(self, male):
        self.driver.find_element(By.XPATH, "//input[@id='NumberOfMaleEmployees']").send_keys(male)

    def enter_no_of_female_employees(self, female):
        self.driver.find_element(By.XPATH, "//input[@id='NumberOfFemaleEmployees']").send_keys(female)

    def enter_contact_person(self, person):
        self.driver.find_element(By.XPATH, "//input[@id='ContactPerson']").send_keys(person)

    def enter_title(self, title):
        self.driver.find_element(By.XPATH, "//input[@id='Title']").send_keys(title)
   
    def enter_name_of_company(self, company):
        self.driver.find_element(By.XPATH, "//input[@id='OrganisationName']").send_keys(company)

    def enter_street_address(self, street):
        self.driver.find_element(By.XPATH, "//input[@id='StreetAddress']").send_keys(street)

    def save_btn(self):
        self.driver.find_element(By.XPATH, "//input[@value='Save']").click()

    


