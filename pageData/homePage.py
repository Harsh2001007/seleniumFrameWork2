from selenium.webdriver.common.by import By


class Homepageclass:
    def __init__(self, driver):
        self.driver = driver

    searchbarSelector = (
        By.XPATH,
        "//input[@placeholder='Search by City, University or Property']",
    )
    loginbtnSelector = (By.XPATH, "//span[text()='Login / SignUp']")
    homepageImgSelector = (By.XPATH, "//img[@alt='University Living']")
    headerServicesSelector = (By.XPATH, "//a[text()='Services']")
    roomreplacementSelector = (By.XPATH, "//a[@href = '/services/room-replacement']")
    servicesSelector = (By.XPATH, "//a[text()='Services']")
    contactusSelector = (By.XPATH, "//a[text()='Contact Us']")
    headerSearchSelector = (
        By.XPATH,
        "//input[@placeholder='Search by City, University or Property']",
    )
    chatIcon_Selector = (By.XPATH, "//img[@alt='Chat Icon']")
    search_results_selector = (
        By.XPATH,
        "//div[@id='async-pagination-example']/div/a/div/div[1]",
    )
    downloadApp_link_selector = (By.XPATH, "//div[text()='Download App']")
    flightTickets_link_selector = (By.XPATH, "//div[text()='Flight Tickets']")
    about_link_selector = (By.XPATH, "//div[text()='About']")
    blog_link_selector = (By.XPATH, "//div[text()='Blog']")
    careers_link_selector = (By.XPATH, "//div[text()='Careers']")
    referAndearn_link_selector = (By.XPATH, "//div[text()='Refer & Earn']")
    costOfliving_link_selector = (By.XPATH, "//a[text()='Cost of Living']")
    findMyKindaRoom_link_selector = (By.XPATH, "//a[text()='Find My Kinda Room']")
    services_link_selector = (By.XPATH, "//a[text()='Services']")
    scholarship_link_selector = (By.XPATH, "//a[text()='Scholarship']")
    hero_title_selector = (By.XPATH, "//p[text()='Safe home for every student']")
    hero_kinda_selector = (By.XPATH, "//p[text()='Find My Kinda Room']")
    hero_trust_pilot_selector = (By.XPATH, "(//img[@alt='Trustpilot'])[1]")
    hero_video_reviews_selector = (By.XPATH, "//button[text()='Video Reviews']")
    hero_kinda_desc_selector = (
        By.XPATH,
        "//p[text()='Curated recommendations from experts']",
    )
    bedsCount_selector = (By.XPATH, "//p[text()='1.75 Mn+']")
    bedsText_selector = (By.XPATH, "//p[text()='Beds']")
    propertiesCount_selector = (By.XPATH, "//p[text()='35K+']")
    propertiesText_selector = (By.XPATH, "//p[text()='Properties']")
    studentAssistedCount_selector = (By.XPATH, "//p[text()='2 Mn']")
    studentAssistedText_selector = (By.XPATH, "//p[text()='students Assited']")
    globalCitiesCount_selector = (By.XPATH, "//p[text()='300+']")
    globalCitiestext_selector = (By.XPATH, "//p[text()='Global Cities']")

    # ---------------------------Top citites selector -----------------------------------------------

    londonImage_selector = (By.XPATH, "//img[@alt='London']")
    nottinghamImage_selector = (By.XPATH, "//img[@alt='Nottingham']")
    leedsImage_selector = (By.XPATH, "//img[@alt='Leeds']")
    melbourneImage_selector = (By.XPATH, "//img[@alt='Melbourne']")
    birminghamImage_selector = (By.XPATH, "//img[@alt='Birmingham']")
    liverpoolImage_selector = (By.XPATH, "//img[@alt='Liverpool']")
    torontoImage_selector = (By.XPATH, "//img[@alt='Toronto']")
    newyorkImage_selector = (By.XPATH, "//img[@alt='New York']")

    # ----------------------- Top cities names -----------------------------

    cityNames_selector = (
        By.XPATH,
        "/html/body/div[1]/main/section[3]/div[2]/a/div/div/div/span[1]",
    )

    bedsCount_selector = (
        By.XPATH,
        "/html/body/div[1]/main/section[3]/div[2]/a/div/div/div/span[2]",
    )

    # -------------------------- perfect home section ------------------------------

    Title_selector = (By.XPATH, "//div[text()='Let us find your perfect home!']")
    descOne_selector = (By.XPATH, "//p[text()='Search - Compare - Relax']")
    descTwo_selector = (By.XPATH, "//p[text()='Easy Peasy']")
    descThree_selector = (By.XPATH, "//p[text()='Price Match Guarantee']")
    termsAndConditions_selector = (By.XPATH, "//a[text()='Terms & Conditions']")

    # ---------------------------popular Properties ---------------------------
    vertCityNames_selector = (By.XPATH, "//ul[@class='p-4 space-y-11']/li")
    uk_selector = (By.ID, "united-kingdom")
    australia_selector = (By.ID, "australia")
    ireland_selector = (By.ID, "ireland")
    canada_selector = (By.ID, "canada")
    us_selector = (By.ID, "united-states")
    popPropertiesNames_selector = (
        By.XPATH,
        "//div[@class='w-[85vw] md:w-[45vw] flex-shrink-0 lg:w-full flex flex-col text-theme-black-text']/a/p[1]",
    )
    popPropertiesPrice_selector = (
        By.XPATH,
        "//div[@class='w-[85vw] md:w-[45vw] flex-shrink-0 lg:w-full flex flex-col text-theme-black-text']/a/p[2]",
    )
    popCountries_selector = (
        By.XPATH,
        "//div[@class='flex items-center justify-between mb-4 md:mb-8']/ul/li",
    )

    # -------------------- Our services section -----------------------------------------

    servicesTitle_selector = (By.XPATH, "//div[text()='Our Services']")
    servicesNames_selector = (By.XPATH, "//div[@class='my-auto pr-4']/p[1]")
    accommodation_service_selector = (By.XPATH, "(//p[text()='Accommodation'])[2]")
    studentFlight_service_selector = (
        By.XPATH,
        "(//p[text()='Student Flight Tickets'])[2]",
    )
    guarantor_service_selctor = (By.XPATH, "(//p[text()='Guarantor'])[2]")

    # --------------------- Trending Articles section ----------------------------

    aricleTitle_selector = (By.XPATH, "//div[text()='Trending Articles']")
    articleHeading_selector = (By.XPATH, "//div[@class='overflow p-4']/p")

    # ---------------- Review section ---------------------------------------

    reviewTitle_selector = (By.XPATH, "//div[text()='What Students Say About Us']")
    reviewsNames_selector = (By.XPATH, "//div[@class='overflow p-4']/p")

    # -------------- Media spotlight section ---------------------------------

    mediaTitleSelector = (By.XPATH, "//div[text()='Media Spotlight']")
    mediaSpotlightCardsSelector = (By.XPATH, "//a[@class='flex-shrink-0']")
    mediaSpotlightViewAll_selector = (By.XPATH, "(//div[text()='View All'])[5]")
    # ---------------------- Seo Description section -----------------------

    seotitle_selector = (
        By.XPATH,
        "//h2[text()='The Ultimate Overseas Student Accommodation Solution']",
    )

    # ---------------------------- Footer section -----------------------------------

    footerServices_selector = (
        By.XPATH,
        "//div[@class='basis-5/12 lg:pr-2 lg:m-0 mt-6']/ul/li/a/p[1]",
    )
    companyLinks_selector = (
        By.XPATH,
        "//div[@class='basis-1/2 lg:basis-4/12 pr-4 lg:m-0 mt-5']/ul/li/a/p[1]",
    )

    # ----------------------------- newsletter section --------------------------------

    newsLetterEmail_selector = (By.XPATH, "//input[@placeholder='Your Email']")
    newsLetterSubscribe_selector = (By.XPATH, "//div[text()='Subscribe']")
    closeBtnSubscribe_selector = (
        By.XPATH,
        "//button[@class='z-[2] p-1.5 absolute rounded-full border leading-none outline-none focus:outline-none transition-colors -top-2 -right-2 md:-top-3 md:-right-3 bg-white border-gray-300 hover:bg-gray-100']",
    )

    # -------------------------------------- Request widgets ---------------------------------

    callIcon_selector = (By.ID, "supportSystem")
    getACallIcon_selector = (By.XPATH, "(//div[@class='relative']/div)[2]")
    whatsappIcon_selector = (By.XPATH, "(//div[@class='relative']/div)[1]")

    # ------------------------------Methods ------------------------------
    def searchbar(self):
        return self.driver.find_element(*Homepageclass.searchbarSelector)

    def loginBtn(self):
        return self.driver.find_element(*Homepageclass.loginbtnSelector)

    def headerLogo(self):
        return self.driver.find_element(*Homepageclass.homepageImgSelector)

    def headerServices(self):
        return self.driver.find_element(*Homepageclass.headerServicesSelector)

    def roomReplacement(self):
        return self.driver.find_element(*Homepageclass.roomreplacementSelector)

    def services(self):
        return self.driver.find_element(*Homepageclass.servicesSelector)

    def contactus(self):
        return self.driver.find_element(*Homepageclass.contactusSelector)

    def headerSearch(self):
        return self.driver.find_element(*Homepageclass.headerSearchSelector)

    def chatIcon(self):
        return self.driver.find_element(*Homepageclass.chatIcon_Selector)

    def search_results(self):
        return self.driver.find_elements(*Homepageclass.search_results_selector)

    def download_app(self):
        return self.driver.find_element(*Homepageclass.downloadApp_link_selector)

    def About(self):
        return self.driver.find_element(*Homepageclass.about_link_selector)

    def Blog(self):
        return self.driver.find_element(*Homepageclass.blog_link_selector)

    def careers(self):
        return self.driver.find_element(*Homepageclass.careers_link_selector)

    def referAndearn(self):
        return self.driver.find_element(*Homepageclass.referAndearn_link_selector)

    def flight_tickets(self):
        return self.driver.find_element(*Homepageclass.flightTickets_link_selector)

    def cost_of_living(self):
        return self.driver.find_element(*Homepageclass.costOfliving_link_selector)

    def find_my_kinda_room(self):
        return self.driver.find_element(*Homepageclass.findMyKindaRoom_link_selector)

    def services(self):
        return self.driver.find_element(*Homepageclass.services_link_selector)

    def scholarship(self):
        return self.driver.find_element(*Homepageclass.scholarship_link_selector)

    def heroTitle(self):
        return self.driver.find_element(*Homepageclass.hero_title_selector)

    def heroKinda(self):
        return self.driver.find_element(*Homepageclass.hero_kinda_selector)

    def heroTrustPilot(self):
        return self.driver.find_element(*Homepageclass.hero_trust_pilot_selector)

    def heroVideoReview(self):
        return self.driver.find_element(*Homepageclass.hero_video_reviews_selector)

    def heroKindaDesc(self):
        return self.driver.find_element(*Homepageclass.hero_kinda_desc_selector)

    # ----------------------------Top cities images --------------------------------------

    def londonImg(self):
        return self.driver.find_element(*Homepageclass.londonImage_selector)

    def nottinghamImg(self):
        return self.driver.find_element(*Homepageclass.nottinghamImage_selector)

    def leedsImg(self):
        return self.driver.find_element(*Homepageclass.leedsImage_selector)

    def melbourneImg(self):
        return self.driver.find_element(*Homepageclass.melbourneImage_selector)

    def birminghamImg(self):
        return self.driver.find_element(*Homepageclass.birminghamImage_selector)

    def liverpoolImg(self):
        return self.driver.find_element(*Homepageclass.liverpoolImage_selector)

    def torontoImg(self):
        return self.driver.find_element(*Homepageclass.torontoImage_selector)

    def newyorkImg(self):
        return self.driver.find_element(*Homepageclass.newyorkImage_selector)

    # -------------------- Top cities names -----------------------------------

    def topCityNames(self):
        return self.driver.find_elements(*Homepageclass.cityNames_selector)

    def bedsCount(self):
        return self.driver.find_elements(*Homepageclass.bedsCount_selector)

    # --------------------------- perfect home section -------------------

    def title(self):
        return self.driver.find_element(*Homepageclass.Title_selector)

    def descOne(self):
        return self.driver.find_element(*Homepageclass.descOne_selector)

    def descTwo(self):
        return self.driver.find_element(*Homepageclass.descTwo_selector)

    def descThree(self):
        return self.driver.find_element(*Homepageclass.descThree_selector)

    def TandCperfecthome(self):
        return self.driver.find_element(*Homepageclass.termsAndConditions_selector)

    # ------------------------------ Popular Properties ----------------------------

    def popUK(self):
        return self.driver.find_element(*Homepageclass.uk_selector)

    def popAUS(self):
        return self.driver.find_element(*Homepageclass.australia_selector)

    def popIRE(self):
        return self.driver.find_element(*Homepageclass.ireland_selector)

    def popCAN(self):
        return self.driver.find_element(*Homepageclass.canada_selector)

    def popUS(self):
        return self.driver.find_element(*Homepageclass.us_selector)

    def vertCityNames(self):
        return self.driver.find_elements(*Homepageclass.vertCityNames_selector)

    def popularPropertiesNames(self):
        return self.driver.find_elements(*Homepageclass.popPropertiesNames_selector)

    def popularPropertiesPrice(self):
        return self.driver.find_elements(*Homepageclass.popPropertiesPrice_selector)

    def popCountryNames(self):
        return self.driver.find_elements(*Homepageclass.popCountries_selector)

    # ----------------------services methods ----------------------------

    def servicesTitle(self):
        return self.driver.find_element(*Homepageclass.servicesTitle_selector)

    def servicesHomepage(self):
        return self.driver.find_elements(*Homepageclass.servicesNames_selector)

    def accommodationService(self):
        return self.driver.find_element(*Homepageclass.accommodation_service_selector)

    def studentFlightService(self):
        return self.driver.find_element(*Homepageclass.studentFlight_service_selector)

    def guarantorService(self):
        return self.driver.find_element(*Homepageclass.guarantor_service_selctor)

    # ---------------------- Review section methods ----------------------------

    def reviewTitle(self):
        return self.driver.find_element(*Homepageclass.reviewTitle_selector)

    def reviewNames(self):
        return self.driver.find_elements(*Homepageclass.reviewsNames_selector)

    # -----------------------media spotlight methods ----------------

    def mediaSpotlightTitle(self):
        return self.driver.find_element(*Homepageclass.mediaTitleSelector)

    def mediaSpotlightCards(self):
        return self.driver.find_elements(*Homepageclass.mediaSpotlightCardsSelector)

    def mediaSportLightViewAllBtn(self):
        return self.driver.find_element(*Homepageclass.mediaSpotlightViewAll_selector)

    # --------------------- SEO description Methods ---------------------

    def seoTitle(self):
        return self.driver.find_element(*Homepageclass.seotitle_selector)

    # ------------------------ Footer services --------------------------

    def footerServices(self):
        return self.driver.find_elements(*Homepageclass.footerServices_selector)

    def companyLInks(self):
        return self.driver.find_elements(*Homepageclass.companyLinks_selector)

    # ------------------------newsletter section ------------------------------

    def newsLetterEmail(self):
        return self.driver.find_element(*Homepageclass.newsLetterEmail_selector)

    def newsLetterSubscribe(self):
        return self.driver.find_element(*Homepageclass.newsLetterSubscribe_selector)

    def closeBtnSubscribe(self):
        return self.driver.find_element(*Homepageclass.closeBtnSubscribe_selector)

    # ------------------------------ call icon widget methods -------------------------

    def callIcon(self):
        return self.driver.find_element(*Homepageclass.callIcon_selector)

    def getACall(self):
        return self.driver.find_element(*Homepageclass.getACallIcon_selector)

    def whatsapp(self):
        return self.driver.find_element(*Homepageclass.whatsappIcon_selector)
