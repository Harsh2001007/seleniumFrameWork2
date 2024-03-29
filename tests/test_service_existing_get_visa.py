from pytest import mark
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.getVisa import GetVisaClass


N = 10


class Test_Existing_Bank_Account(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/visa-assistance"

    def test_Existing_Bank_Account(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        visa = GetVisaClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Get Visa']").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\selenium_things\\selenium_framework\\screenshots\\services\\get_visa\\visaHome.png"
        )

        assert self.driver.current_url == Test_Existing_Bank_Account.page_url

        visa.submitBtn().click()
        time.sleep(1)

        assert visa.firstNameError().is_displayed()
        assert visa.lastNameError().is_displayed()
        assert visa.emailError().is_displayed()
        assert visa.phoneNumberError().is_displayed()

        visa.firstName().send_keys("test")
        visa.lastName().send_keys("test")
        visa.email().send_keys("harsh.sachan@universityliving.com")
        visa.phoneNumber().send_keys("8505813979")
        visa.submitBtn().click()

        login.loginMethod()

        visa.submitBtn().click()
        time.sleep(3)
        redirection_Url_getVisa = self.driver.current_url
        log.info("get visa redirection url -> " + redirection_Url_getVisa)

        visa.okBtn().click()
        time.sleep(2)
