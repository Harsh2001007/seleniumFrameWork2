from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import string
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="C://Users//TUL//Desktop//selenium_things//selenium_framework//logs&Repos//Uninist-Logs//test.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

N = 10

# List of URLs to automate
urls = [
    "https://uninist.com/student-accommodations-liverpool",
    "https://uninist.com/student-accommodations-birmingham",
    "https://uninist.com/student-accommodations-sheffield",
    "https://uninist.com/student-accommodations-manchester",
    "https://uninist.com/student-accommodations-leeds",
]


# Initialize the WebDriver
driver = (
    webdriver.Chrome()
)  # You may need to provide the path to your ChromeDriver executable

driver.maximize_window()

driver.implicitly_wait(10)
# Loop through each URL
for url in urls:
    res = "".join(random.choices(string.ascii_lowercase + string.digits, k=N))
    new_email = res + "@yopmail.com"
    new_phoneNumber = "".join([str(random.randint(0, 9)) for i in range(10)])
    driver.get(url)

    time.sleep(3)

    urlLastWord = url.split("/")[-1]
    cityName = urlLastWord.split("-")[-1]

    print("for the url -->", url)
    logging.info("url ->", url)

    # First Name field
    first_name_field = driver.find_element(By.NAME, "fName")
    first_name_field.send_keys("Test")
    logging.info("First name -> Test ")

    # Last Name field
    last_name_field = driver.find_element(By.NAME, "lName")
    last_name_field.send_keys("test" + cityName)
    logging.info("Last name -> test", cityName)

    # Email Field
    email_field = driver.find_element(By.NAME, "fEmail")
    email_field.send_keys(new_email)
    print(new_email)
    logging.info("used email -> ", new_email)

    # handling Flag
    flag = driver.find_element(By.XPATH, "//div[@class='iti__selected-flag']")
    flag.click()

    # handling Phone Number Country search bar
    phone_country_code = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    phone_country_code.send_keys("india")

    # Handling Indian Flag Selection
    indiaCountryFlag = driver.find_element(By.XPATH, "//span[text()='India']")
    indiaCountryFlag.click()

    # Handling Phone Number Field (insertion)
    phone_field = driver.find_element(By.ID, "phone")
    phone_field.send_keys(new_phoneNumber)
    print(new_phoneNumber)
    logging.info("phone number used -> ", new_phoneNumber)

    # Handling home country field
    home_country_field = driver.find_element(By.NAME, "nationality")
    homeCountry = Select(home_country_field)
    homeCountry.select_by_index(2)

    # Handling preferred budget field
    preferred_budget_field = driver.find_element(By.NAME, "fBudgets")
    preferedBudget = Select(preferred_budget_field)
    preferedBudget.select_by_index(2)

    # Handling message field
    message_field = driver.find_element(By.NAME, "fMessage")
    message_field.send_keys("This is a test message.")
    logging.info("test message -> This is a test message.")

    # Handling check out date field
    check_out_date_field = driver.find_element(By.NAME, "fCheckOut")
    check_out_date_field.click()
    time.sleep(2)
    checkoutdate30 = driver.find_element(By.XPATH, "//td[text()='30']")
    checkoutdate30.click()
    print("check out date -> 30th of current month")
    logging.info("check out date -> 30th of current month")

    # Handling checkbox element
    checkbox_element = driver.find_element(By.ID, "flexRadioDefault1")
    checkbox_element.click()

    # Handling check in date field
    check_in_date_field = driver.find_element(By.NAME, "fCheckIn")
    check_in_date_field.click()
    time.sleep(3)
    check_in_date_field.send_keys(Keys.ENTER)
    print("check in date in today's date")
    logging.info("check in date in today's date")

    # Handling submit button
    submit_button = driver.find_element(
        By.XPATH, "//button[text()=' Find a room for me ']"
    )
    submit_button.click()

    time.sleep(5)

# Close the WebDriver
driver.quit()
