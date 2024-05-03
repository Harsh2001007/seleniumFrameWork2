import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.FlightTickets import FlightTicketClass


N = 10


class Test_Existing_Student_Flight_Tickets(Invokation):
    email = "harsh.sachan@universityliving.com"
    phoneNumber = "8505813979"
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/students-flight-ticket"

    def test_Existing_Student_Flight_Tickets(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)
        login = loginpopupClass(self.driver)
        flt = FlightTicketClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(
            By.XPATH, "//p[text()='Student Flight Tickets']"
        ).click()
        time.sleep(2)
        self.driver.refresh()

        assert self.driver.current_url == Test_Existing_Student_Flight_Tickets.page_url

        flt.toDestination().click()
        flt.toCitySearchDublin().click()
        flt.returnDate().click()
        flt.lastDate().click()
        flt.travellerAndClass().click()
        flt.searchFlightsBtn().click()

        # login.emailfield().send_keys(Test_Existing_Student_Flight_Tickets.email.lower())
        # login.loginBtn().click()
        # login.otpFirst().send_keys("1")
        # login.otpsecond().send_keys("2")
        # login.otpthird().send_keys("3")
        # login.otpfourth().send_keys("4")
        # login.otpfifth().send_keys("5")
        # login.continueBtn().click()
        login.loginMethod()

        flt.searchFlightsBtn().click()
        flt.submitBtn().click()
        time.sleep(3)
        roundTrip_redirection_url = self.driver.current_url
        log.info("redirection url of round trip-> " + roundTrip_redirection_url)

        self.driver.back()

        # ------------------------- checking for one way --------------------------

        flt.oneWay().click()
        flt.toDestination().click()
        flt.toCitySearchDublin().click()
        flt.travellerAndClass().click()
        flt.searchFlightsBtn().click()
        flt.submitBtn().click()
        time.sleep(3)
        oneWay_redirection_url = self.driver.current_url
        log.info("redirection url of one way-> " + oneWay_redirection_url)
        time.sleep(3)
        self.driver.back()

        time.sleep(3)
