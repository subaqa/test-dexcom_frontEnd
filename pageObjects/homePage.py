import logging
from selenium.webdriver.common.by import By
import utilities.dex_logger as cl

class HomePage:
    log = cl.getLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    welcomeMessageSelector = "//div[@class='main-landing']/header/h1"
    homeUserSectionSelector = (By.XPATH, "//li[@class='panel home-user']/h2")
    homeUserLoginSelector = (By.XPATH, "//a[@href='/users/auth/dexcom_sts']")

    def getWelcomeMessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.welcomeMessageSelector)
        except:
            self.log.info("Unable to locate Welcome message element")

    def getHomeUserSection(self):
        try:
            return self.driver.find_element(*HomePage.homeUserSectionSelector)
        except:
            self.log.info("Unable to locate Home user section")

    def getHomeUserLogin(self):
        try:
            return self.driver.find_element(*HomePage.homeUserLoginSelector)
        except:
            self.log.info("Unable to locate Home user login link ELement")

    def clickHomeUserLinkClick(self):
        try:
            self.getHomeUserLogin().click()
        except:
            self.log.info("Unable to click the home user link")

    def homeUsersLinkAccess(self):
        # validate the page header
        assert "Welcome to Dexcom CLARITY" in self.getWelcomeMessage().text
        # validating home user section is available
        assert "Home User" in self.getHomeUserSection().text
        # Click on home user link should take to dexcom login page
        self.clickHomeUserLinkClick()


