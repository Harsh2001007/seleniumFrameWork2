from selenium.webdriver.common.by import By


class getacallClass:
    def __init__(self, driver):
        self.driver = driver

    firstName_selector = (By.NAME, "firstName")
    lasttName_selector = (By.NAME, "lastName")
    email_selector = (By.NAME, "email")
    phonenumber_selector = (By.ID, "contactNumber")
    requestCallbackBtn_selector = (By.XPATH, "//div[text()='Request Callback']")
    scheduleCallbackBtn_selector = (By.XPATH, "//div[text()='Schedule Callback']")
    selectUni_selector = (By.XPATH, "//input[@placeholder='Select University']")
    universityId_selector = (By.ID, "university-search-item-1")
    requestCallbackSuccess_selector = (
        By.XPATH,
        "//p[text()='Thanks for requesting a call. Our team of experts will be in touch with you soon.']",
    )
    successModalClose_selector = (
        By.XPATH,
        "//button[@class='z-[2] p-1.5 absolute rounded-full border leading-none outline-none focus:outline-none transition-colors -top-2 -right-2 md:-top-3 md:-right-3 bg-white border-gray-300 hover:bg-gray-100']",
    )

    calendarInput_selector = (By.ID, "date")
    calendarDate30_selector = (By.XPATH, "//td[text()='30']")
    timing_selector = (By.ID, "callTiming")
    calendarDate27_selector = (By.XPATH, "(//td[text()='27'])[2]")
    timing_selector = (By.ID, "callTiming")

    scheduleCallbackSuccess_selector = (
        By.XPATH,
        "//p[text()='Thanks for scheduling a call. Our team of experts will be in touch with you at scheduled time.']",
    )

    submitBtn_selector = (By.XPATH, "//div[text()='Submit']")
    scheduleCallMonFriErro_selector = (
        By.XPATH,
        "//p[text()='Call can be scheduled for Mon - Fri']",
    )
    # ------------------ methods -----------------

    def firstName(self):
        return self.driver.find_element(*getacallClass.firstName_selector)

    def lastName(self):
        return self.driver.find_element(*getacallClass.lasttName_selector)

    def email(self):
        return self.driver.find_element(*getacallClass.email_selector)

    def phoneNumber(self):
        return self.driver.find_element(*getacallClass.phonenumber_selector)

    def requestCallbackBtn(self):
        return self.driver.find_element(*getacallClass.requestCallbackBtn_selector)

    def scheduleCallbackBtn(self):
        return self.driver.find_element(*getacallClass.scheduleCallbackBtn_selector)

    def selectUni(self):
        return self.driver.find_element(*getacallClass.selectUni_selector)

    def universityId(self):
        return self.driver.find_element(*getacallClass.universityId_selector)

    def requestCallbackSuccess(self):
        return self.driver.find_element(*getacallClass.requestCallbackSuccess_selector)

    def successModalCloseBtn(self):
        return self.driver.find_element(*getacallClass.successModalClose_selector)

    def calendarInput(self):
        return self.driver.find_element(*getacallClass.calendarInput_selector)

    def calendarDate30(self):
        return self.driver.find_element(*getacallClass.calendarDate30_selector)

    def calendarDate27(self):
        return self.driver.find_element(*getacallClass.calendarDate27_selector)

    def timing(self):
        return self.driver.find_element(*getacallClass.timing_selector)

    def scheduleSuccess(self):
        return self.driver.find_element(*getacallClass.scheduleCallbackSuccess_selector)

    def submitBtn(self):
        return self.driver.find_element(*getacallClass.submitBtn_selector)

    def schedulecallMonFriErro(self):
        return self.driver.find_element(*getacallClass.scheduleCallMonFriErro_selector)
