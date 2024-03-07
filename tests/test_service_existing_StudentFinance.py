import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.studentFinancing import StudentFinancingClass
from pageData.header import Headerclass

N = 10


class Test_Existing_Student_Financing(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/student-finance"

    def test_Existing_Student_Financing(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        studentFinance = StudentFinancingClass(self.driver)
        header = Headerclass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Student Financing']").click()
        time.sleep(2)

        # ---------------------------------- ICICI bank ---------------------------------

        studentFinance.submitBtn().click()

        assert studentFinance.firstNameError().is_displayed()
        assert studentFinance.lastNameError().is_displayed()
        assert studentFinance.emailError().is_displayed()
        assert studentFinance.phoneNumberError().is_displayed()

        header.loginBtn().click()
        login.loginMethod()

        countryDropdown = Select(studentFinance.country())
        countryDropdown.select_by_index(2)
        providerDropdown = Select(studentFinance.provider())
        providerDropdown.select_by_index(2)

        studentFinance.submitBtn().click()
        time.sleep(2)
        log.info("Gyandhan redirection url ->" + self.driver.current_url)
        studentFinance.okBtn().click()

        providerDropdownTwo = Select(studentFinance.provider())
        providerDropdownTwo.select_by_index(3)
        studentFinance.submitBtn().click()
        time.sleep(2)
        log.info("HDFC redirection url ->" + self.driver.current_url)
        studentFinance.okBtn().click()

        providerDropdownTwo = Select(studentFinance.provider())
        providerDropdownTwo.select_by_index(1)
        studentFinance.submitBtn().click()
        time.sleep(5)
        log.info("ICIC redirection url ->" + self.driver.current_url)
