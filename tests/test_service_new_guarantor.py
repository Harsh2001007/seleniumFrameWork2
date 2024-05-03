import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.Guarnator import GuarantorClass
import string
import random

N = 10


class Test_New_Guarantor(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/guarantor"

    def test_New_Guarantor(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        guarantor = GuarantorClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Guarantor']").click()
        time.sleep(2)
        self.driver.refresh()
        assert self.driver.current_url == Test_New_Guarantor.page_url

        countryDropDown = Select(self.driver.find_element(By.ID, "country"))
        countryDropDown.select_by_visible_text("UK")
        guarantor.findGuarantorBtn().click()

        login.emailfield().send_keys(Test_New_Guarantor.new_email.lower())
        log.info("used new email in service - FL ->" + Test_New_Guarantor.new_email)
        login.loginBtn().click()
        login.firstName().send_keys("test")
        login.lastName().send_keys("test")
        login.phoneNumber().send_keys(Test_New_Guarantor.new_phoneNumber)
        log.info(
            "used new phone number in service - FL ->"
            + Test_New_Guarantor.new_phoneNumber
        )
        login.signUpBtn().click()
        login.otpFirst().send_keys("1")
        login.otpsecond().send_keys("2")
        login.otpthird().send_keys("3")
        login.otpfourth().send_keys("4")
        login.otpfifth().send_keys("5")
        login.continueBtn().click()

        guarantor.findGuarantorBtn().click()
        guarantor.formSubmitBtn().click()

        time.sleep(3)
        redirectionUrl = self.driver.current_url
        log.info("UK - Redirection Url -> " + redirectionUrl)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
