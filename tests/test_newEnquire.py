import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECchromedriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.common.exceptions import NoSuchElementException
import pytest
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.loginPopup import loginpopupClass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass
import pytest
import string
import random

N = 7
class Test_NewuserEnquireForm(Invokation):
    
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    newEmail = res+"@yopmail.com"
        
    enquireNowUrl = "https://www.universityliving.com/united-kingdom/london/iq-hoxton/enquire-now/thank-you"
    
    def test_enquireE2e(self):
        
        log = self.getLogger()
        
        self.driver.implicitly_wait(5)
        
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        enquireformObj = FormClass(self.driver)
        homepageObj.searchbar().send_keys("iq hoxton")
        self.driver.find_element(By.XPATH,"//div[text()='iQ Hoxton']").click()
        detailpageObj.enquireButton().click()
        enquireformObj.firstName().send_keys("test")
        enquireformObj.lastName().send_keys("test")
        enquireformObj.email().send_keys(Test_NewuserEnquireForm.newEmail)
        enquireformObj.phoneNumber().send_keys("8505813979")
        enquireformObj.message().send_keys("this is test message :)")
        visastatusDropdown = Select(enquireformObj.visaStatus())
        visastatusDropdown.select_by_index(3)
        bestPlatformDropdown = Select(enquireformObj.platform())
        bestPlatformDropdown.select_by_index(10)
        enquireformObj.platformInfo().send_keys("Discord-ID-Test-1234")
        try:
            enquireformObj.uniIDone().click()
        except Exception:
            try:
                enquireformObj.uniIDtwo().click()
            except Exception:
                try:
                    enquireformObj.uniIDthree().click()
                except:
                    try:
                        enquireformObj.uniIDfour().click()
                    except Exception:
                        print('id is not available for the univerisity select field')
           
        enquireformObj.uniItem().click()
        enquireformObj.submitBtnEnquire().click()
        time.sleep(5)
        currenturl = self.driver.current_url
        
        assert Test_NewuserEnquireForm.enquireNowUrl == currenturl
            # print("test success")
        # else:
        #     print("test failed")

        print(currenturl)
        print(Test_NewuserEnquireForm.newEmail)
        log.info("new email id is " + Test_NewuserEnquireForm.newEmail)