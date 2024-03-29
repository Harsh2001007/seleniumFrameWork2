import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
from pageData.detailPage import detailpageClass
from pageData.Forms import FormClass


class Test_Enquire_exisitng_user(Invokation):
    iq_hoxton_thankYou_url = "https://www.universityliving.com/united-kingdom/london/iq-hoxton/enquire-now/thank-you"
    chapter_ealing_thankYou_url = "https://www.universityliving.com/united-kingdom/london/chapter-ealing/enquire-now/thank-you"
    scape_melbourne_central_thankyou_url = "https://www.universityliving.com/australia/melbourne/scape-melbourne-central/enquire-now/thank-you"

    def test_enquire_form_existing_user(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homepageObj = Homepageclass(self.driver)
        detailpageObj = detailpageClass(self.driver)
        enquireformObj = FormClass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        assert homepageObj.searchbar().is_displayed()
        homepageObj.searchbar().send_keys("chapter ealing")
        time.sleep(3)
        homepageObj.searchbar().send_keys(Keys.ENTER)
        try:
            detailpageObj.enquireButton().click()
            log.info("IQ hoxton - Enquire Now")
        except Exception:
            homepageObj.headerSearch().send_keys("chapter ealing")
            time.sleep(2)
            homepageObj.headerSearch().send_keys(Keys.ENTER)
            try:
                detailpageObj.enquireButton().click()
                log.info("chapter ealing - Enquire now")
            except Exception:
                homepageObj.headerSearch().send_keys("scape melbourne central")
                time.sleep(2)
                homepageObj.headerSearch().send_keys(Keys.ENTER)
                detailpageObj.enquireButton().click()
                log.info("scape melbourne central - Enquire Now")
        enquireformObj.firstName().clear()
        enquireformObj.firstName().send_keys("test")
        enquireformObj.lastName().clear()
        enquireformObj.lastName().send_keys("test")
        enquireformObj.email().clear()
        enquireformObj.email().send_keys("harsh.sachan@universityliving.com")
        for i in range(10):
            enquireformObj.phoneNumber().send_keys(Keys.BACKSPACE)
        enquireformObj.phoneNumber().send_keys("8505813979")
        enquireformObj.message().clear()
        enquireformObj.message().send_keys("this is test message :)")
        bestPlatformDropdown = Select(enquireformObj.platform())
        bestPlatformDropdown.select_by_index(10)
        enquireformObj.platformInfo().send_keys("Discord-ID")
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
                        try:
                            enquireformObj.uniIDfive().click()
                        except Exception:
                            log.warning(
                                "id is not available for the univerisity select field"
                            )
        enquireformObj.uniItem().click()

        nationalityDropDown = Select(enquireformObj.nationalityDrop())
        nationalityDropDown.select_by_index(3)

        enquireformObj.submitBtnEnquire().click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(
            "C:\\Users\\TUL\\Desktop\\FrameWorkDesign2\\logs&Repos\\forms\\enquireNow.png"
        )
        currenturl = self.driver.current_url
        if (
            currenturl == Test_Enquire_exisitng_user.iq_hoxton_thankYou_url
            or currenturl == Test_Enquire_exisitng_user.chapter_ealing_thankYou_url
            or currenturl
            == Test_Enquire_exisitng_user.scape_melbourne_central_thankyou_url
        ):
            log.info("Thankyou URL is working Fine")
        else:
            log.warning("Thankyou URL is not working PlZ check")
        homepageObj.headerLogo().click()
