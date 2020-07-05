from selenium.webdriver.common.by import By
import utilities.dex_logger as cl
import logging
from utilities.wait_Explicit import userAction


class UploadPage:
    log = cl.getLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    uploadSectionTabSelector = (By.XPATH, "//div[@id='ember19']/md-list-item/div/div[1]")

    def getUploadSectionTab(self):
        try:
            return self.driver.find_element(*UploadPage.uploadSectionTabSelector)
        except:
            self.log.info("unable to locate upload section tab")

    def verifyElementPresence(self, element):
        try:
            waitElement = userAction(self.driver)
            waitElement.waitForElement(element)
        except:
            self.log.info("Upload section tab is not visible")

    def validateUploadSection(self):
        self.verifyElementPresence("ember70")
        assert "Upload" in self.getUploadSectionTab().text

