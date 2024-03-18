from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import string
from selenium.webdriver.common.keys import Keys

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

    # Find and fill out the fields
    first_name_field = driver.find_element(By.NAME, "fName")
    first_name_field.send_keys("Test")

    last_name_field = driver.find_element(By.NAME, "lName")
    last_name_field.send_keys("Test " + cityName)

    email_field = driver.find_element(By.NAME, "fEmail")
    email_field.send_keys(new_email)
    print(new_email)

    flag = driver.find_element(By.XPATH, "//div[@class='iti__selected-flag']")
    flag.click()

    phone_country_code = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    phone_country_code.send_keys("india")

    indiaCountryFlag = driver.find_element(By.XPATH, "//span[text()='India']")
    indiaCountryFlag.click()

    phone_field = driver.find_element(By.ID, "phone")
    phone_field.send_keys(new_phoneNumber)
    print(new_phoneNumber)

    home_country_field = driver.find_element(By.NAME, "nationality")
    homeCountry = Select(home_country_field)
    homeCountry.select_by_index(2)

    preferred_budget_field = driver.find_element(By.NAME, "fBudgets")
    preferedBudget = Select(preferred_budget_field)
    preferedBudget.select_by_index(2)

    message_field = driver.find_element(By.NAME, "fMessage")
    message_field.send_keys("This is a test message.")

    check_out_date_field = driver.find_element(By.NAME, "fCheckOut")
    check_out_date_field.click()
    time.sleep(2)
    checkoutdate30 = driver.find_element(By.XPATH, "//td[text()='30']")
    checkoutdate30.click()
    print("check out date -> 30th of current month")

    checkbox_element = driver.find_element(By.ID, "flexRadioDefault1")
    checkbox_element.click()

    check_in_date_field = driver.find_element(By.NAME, "fCheckIn")
    check_in_date_field.click()
    time.sleep(3)
    check_in_date_field.send_keys(Keys.ENTER)
    print("check in date in today's date")

    # Example: Find the "Submit" button and click it
    submit_button = driver.find_element(
        By.XPATH, "//button[text()=' Find a room for me ']"
    )
    submit_button.click()

    time.sleep(5)

# Close the WebDriver
driver.quit()


# This script will iterate over each URL, fill out the fields on the webpage, and submit the form. Make sure to replace "University Name" with the appropriate university name if needed and adjust other field locators and values based on the actual structure of the webpages. Also, ensure that you have the correct WebDriver installed and its path provided in the script.
