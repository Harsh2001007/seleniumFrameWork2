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


class Test_request_callback(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    testing_key = "test"
    properties_name = ["chapter ealing", "test (Dev purpose)"]

    def test_requestCallback(self):
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
        Getacall.firstName().send_keys("test")
        Getacall.lastName().send_keys("test")
        Getacall.email().send_keys("test@yopmail.com")
        Getacall.phoneNumber().send_keys("8505813979")
        Getacall.selectUni().click()
        Getacall.universityId().click()
        Getacall.requestCallbackBtn().click()

        if Getacall.requestCallbackSuccess().is_displayed():
            log.info("Request callback successfully placed.")
        else:
            log.warn("There is some issue while placing request callback.")

        Getacall.successModalCloseBtn().click()

        time.sleep(2)
