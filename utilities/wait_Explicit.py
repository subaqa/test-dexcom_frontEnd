from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class userAction():
    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, element):
        elementLocator = None
        try:
            wait = WebDriverWait(self.driver, 15, poll_frequency= 2, ignored_exceptions=
            [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            elementLocator = wait.until(EC.presence_of_element_located((By.ID, element)))
            print("element appeared on the page")
        except:
            print("element not appeared on the page")

        return elementLocator
