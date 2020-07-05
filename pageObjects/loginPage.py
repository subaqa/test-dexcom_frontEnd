import logging
from selenium.webdriver.common.by import By
import utilities.dex_logger as cl


class LoginPage:
    log = cl.getLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # locators
    homeUserLoginPageTitle = (By.CLASS_NAME, "title")
    credentialsSectionSelector = (By.CLASS_NAME, "register-label-left")
    userNameFieldSelector = (By.ID, "username")
    passwordFieldSelector = (By.ID, "password")
    loginButtonSelector = (By.XPATH, "//div[@id='edit-actions']/input[@value='Login']")

    def getloginPageTitle(self):
        try:
            return self.driver.find_element(*LoginPage.homeUserLoginPageTitle)
        except:
            self.log.info("Unable to locate login page title")

    def getCredentialSection(self):
        try:
            return self.driver.find_element(*LoginPage.credentialsSectionSelector)
        except:
            self.log.info("Unable to locate login credential section")

    def getUserNameField(self):
        try:
            return self.driver.find_element(*LoginPage.userNameFieldSelector)
        except:
            self.log.info("Unable to locate username field")

    def getPasswordField(self):
        try:
            return self.driver.find_element(*LoginPage.passwordFieldSelector)
        except:
            self.log.info("Unable to locate password field")

    def getloginButton(self):
        try:
            return self.driver.find_element(*LoginPage.loginButtonSelector)
        except:
            self.log.info("Unable to locate login button")

    def enterUsername(self):
        try:
            self.getUserNameField().send_keys("nilepatest001")
        except:
            self.log.info("Unable to send username value")

    def enterPassword(self):
        try:
            self.getPasswordField().send_keys("Password@1")
        except:
            self.log.info("Unable to send password value")

    def clickLoginButton(self):
        try:
            self.getloginButton().click()
        except:
            self.log.info("Unable to click login button")

    def homeUserLogin(self):
        # validate it takes to the home user login page
        assert "Your Dexcom Account" in self.getloginPageTitle().text
        # validating the user login page section is visible
        assert "Username" in self.getCredentialSection().text
        self.enterUsername()
        self.enterPassword()
        self.clickLoginButton()
