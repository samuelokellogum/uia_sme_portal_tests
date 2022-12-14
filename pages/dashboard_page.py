from selenium.webdriver.common.by import By

class Dashboard:
    # Locators of all the elements    
    dashboard_button_xpath = "//button[normalize-space()='DASHBOARD']"
    
    # Initialise the driver
    def __init__(self, driver):
        self.driver = driver

    # Action method for every element
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    