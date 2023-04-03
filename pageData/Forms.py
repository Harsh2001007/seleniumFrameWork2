from selenium.webdriver.common.by import By

class FormClass:
    def __init__(self,driver):
        self.driver = driver
        
    firstnameSelector = (By.ID,"firstName")
    lastnameSelector = (By.ID,"lastName")
    emailSelector = (By.ID,"email")
    phonenumberSelector = (By.ID,"contactNumber")
    visastatusSelector = (By.NAME,"visaStatus")
    universityID1Selector = (By.ID,":r1:")
    universityID2Selector = (By.ID,":r2:")
    universityID3Selector = (By.ID,":r3:")
    universityID4Selector = (By.ID,":r4:")
    uniItemSelector = (By.ID,"university-search-item-0")
    platformSelector = (By.NAME,"platformToReach")
    platformInfoselector = (By.NAME,"platformInfo")
    messageSelector = (By.ID,"message")
    submitBtnSelector = (By.XPATH,"//div[text()='Submit']")
    BookNowSubmitBtnSelector = (By.XPATH,"(//div[text()='Book Now'])[last()]")
    genderRadioSelector = (By.XPATH,"//span[text()='Male']")
    homeAddressSelector = (By.ID,"g_address")
    countrySelector = (By.NAME,"country")
    stateSelector = (By.ID,"state")
    citySelector = (By.ID,"city")
    postalSelector = (By.ID,"postalCode")
    nationalitySelector = (By.NAME,"nationality")
    nextBtnSelector = (By.XPATH,"//div[text()='Next']")
    courseSelector = (By.NAME,"courseName")
    yearOfstudySelector = (By.NAME,"yearOfStudy")
    startdateSelector = (By.NAME,"startDate")
    startdateMonthSelector = (By.XPATH,"//div[text()='Dec']")
    enddateSelector = (By.NAME,"endDate")
    enddateMonthSelector = (By.XPATH,"//div[text()='Dec']")
    
    
    
    def firstName(self):
        return self.driver.find_element(*FormClass.firstnameSelector)
    
    def lastName(self):
        return self.driver.find_element(*FormClass.lastnameSelector)
    
    def email(self):
        return self.driver.find_element(*FormClass.emailSelector)
    
    def phoneNumber(self):
        return self.driver.find_element(*FormClass.phonenumberSelector)
    
    def visaStatus(self):
        return self.driver.find_element(*FormClass.visastatusSelector)
    
    def uniIDone(self):
        return self.driver.find_element(*FormClass.universityID1Selector)
    
    def uniIDtwo(self):
        return self.driver.find_element(*FormClass.universityID2Selector)
    
    def uniIDthree(self):
        return self.driver.find_element(*FormClass.universityID3Selector)
    
    def uniIDfour(self):
        return self.driver.find_element(*FormClass.universityID4Selector)
    
    def uniItem(self):
        return self.driver.find_element(*FormClass.uniItemSelector)
    
    def platform(self):
        return self.driver.find_element(*FormClass.platformSelector)
    
    def platformInfo(self):
        return self.driver.find_element(*FormClass.platformInfoselector)

    def message(self):
        return self.driver.find_element(*FormClass.messageSelector) 
    
    def submitBtnEnquire(self):
        return self.driver.find_element(*FormClass.submitBtnSelector)   
    
    def bookNowBtn(self):
        return self.driver.find_element(*FormClass.BookNowSubmitBtnSelector)
    
    def genderBtn(self):
        return self.driver.find_element(*FormClass.genderRadioSelector)
    
    def homeField(self):
        return self.driver.find_element(*FormClass.homeAddressSelector)

    def countryDrop(self):
        return self.driver.find_element(*FormClass.countrySelector)

    def stateField(self):
        return self.driver.find_element(*FormClass.stateSelector)

    def cityField(self):
        return self.driver.find_element(*FormClass.citySelector)
    
    def postalField(self):
        return self.driver.find_element(*FormClass.postalSelector)
    
    def nationalityDrop(self):
        return self.driver.find_element(*FormClass.nationalitySelector)

    def nextBtn(self):
        return self.driver.find_element(*FormClass.nextBtnSelector)
    
    def courseField(self):
        return self.driver.find_element(*FormClass.courseSelector)
    
    def yearofstudyField(self):
        return self.driver.find_element(*FormClass.yearOfstudySelector)
    
    def startDateField(self):
        return self.driver.find_element(*FormClass.startdateSelector)

    def endDateField(self):
        return self.driver.find_element(*FormClass.enddateSelector)
    
    def startdateMonth(self):
        return self.driver.find_element(*FormClass.startdateMonthSelector)
    
    def enddateMonth(self):
        return self.driver.find_element(*FormClass.enddateMonthSelector)