import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from invokeBaseClass import Invokation
from pageData.homePage import Homepageclass
import string
import random

N = 10


class Test_New_Student_Finance(Invokation):
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + ".university@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    testing_key = "test"
    page_url = "https://www.universityliving.com/services/student-finance"

    def test_New_Student_Finance(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        homepage = Homepageclass(self.driver)

        try:
            self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        except Exception:
            pass

        hover = ActionChains(self.driver).move_to_element(homepage.services())
        hover.perform()
        self.driver.find_element(By.XPATH, "//p[text()='Student Financing']").click()
        time.sleep(2)
        assert self.driver.current_url == Test_New_Student_Finance.page_url
