from pytest import mark
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.getacall import getacallClass
import string
import random

N = 10


class Test_schedule_callback(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    testing_key = "test"
    properties_name = ["chapter ealing", "test (Dev purpose)"]

    def test_scheduleCallback(self):
        log = self.getLogger()
        self.driver.implicitly_wait(15)
        HomePage = Homepageclass(self.driver)
        Getacall = getacallClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        HomePage.callIcon().click()
        time.sleep(5)
        HomePage.getACall().click()
        Getacall.scheduleCallbackBtn().click()
        Getacall.firstName().send_keys("test")
        Getacall.lastName().send_keys("test")
        Getacall.email().send_keys("test@yopmail.com")
        Getacall.phoneNumber().send_keys("8505813979")
        Getacall.selectUni().click()
        Getacall.universityId().click()
        Getacall.calendarInput().click()
        time.sleep(2)
        Getacall.calendarDate30().click()
        Getacall.submitBtn().click()
        time.sleep(1)
        try:
            if Getacall.schedulecallMonFriErro().is_displayed():
                log.warning("Selected dates are on Saturday or Sunday")
                Getacall.calendarInput().click()
                Getacall.calendarDate27().click()
                Getacall.submitBtn().click()
                log.info("Schedule callback has been made using other date")
                getacallClass.successModalCloseBtn().click()
            else:
                log.critical(
                    "something went wrong while submitting the Schedule callback"
                )
        except Exception:
            if Getacall.scheduleSuccess().is_displayed():
                Getacall.successModalCloseBtn().click()
                log.info("Schedule callback working fine")
            else:
                log.warning(
                    "something went wrong while submitting the schedule callback"
                )

        time.sleep(3)
