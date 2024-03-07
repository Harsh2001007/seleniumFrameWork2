from pytest import mark
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass


class Test_book_now_existing_user(Invokation):
    def test_bookNowForm_existing_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        HomePage = Homepageclass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        HomePage.newsLetterEmail().send_keys("hs5686584@gmail.com")
        HomePage.newsLetterSubscribe().click()
        HomePage.closeBtnSubscribe().click()

        time.sleep(3)

        # need to create assertions for the contact us form.
