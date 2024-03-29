import time
from selenium.webdriver.common.by import By
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass


class Test_Login_existing_user(Invokation):
    def test_login_existing_user(self):
        log = self.getLogger()
        homepageObject = Homepageclass(self.driver)
        loginPopUPObj = loginpopupClass(self.driver)
        loginEmail = "harsh.sachan@universityliving.com"
        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        homepageObject.loginBtn().click()
        loginPopUPObj.emailfield().send_keys(loginEmail)
        loginPopUPObj.loginBtn().click()
        loginPopUPObj.otpFirst().send_keys("1")
        loginPopUPObj.otpsecond().send_keys("2")
        loginPopUPObj.otpthird().send_keys("3")
        loginPopUPObj.otpfourth().send_keys("4")
        loginPopUPObj.otpfifth().send_keys("5")
        loginPopUPObj.continueBtn().click()
        loginPopUPObj.profileIcon().click()
        emailDashboard = loginPopUPObj.dashboardEmail().text
        loginPopUPObj.profileSection().click()
        emailProfile = loginPopUPObj.profileEmail().text
        assert loginEmail == emailDashboard and loginEmail == emailProfile
        if loginEmail == emailDashboard and loginEmail == emailProfile:
            log.info("login successfull + Dashboard data matched")
        else:
            log.warning("dashboard data does not matched wiht login profile")
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\homepage&dashboard\\Login_Dashboard.png"
        )
        homepageObject.headerLogo().click()
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\homepage&dashboard\\After_Login_Homepage.png"
        )
