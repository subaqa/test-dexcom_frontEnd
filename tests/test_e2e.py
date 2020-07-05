from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.uploadPage import UploadPage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_validLogin(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        uploadPage = UploadPage(self.driver)

        homePage.homeUsersLinkAccess()

        loginPage.homeUserLogin()

        uploadPage.validateUploadSection()
