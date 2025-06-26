import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from dotenv import load_dotenv
from os import environ
load_dotenv()

ACCOUNT_EMAIL = environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = environ.get("ACCOUNT_PASSWORD")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
"https://www.linkedin.com/jobs/search/?currentJobId=4245888817&f_LF=f_AL&geoId=102257491&keywords=senior%20software%20engineer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true"
)

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# '/html/body/div[4]/div/div/div[2]/div/div/form/footer/div[3]/button'
# '/html/body/div[4]/div/div/button/svg/use'
# '/html/body/div[4]/div[2]/div/div[3]/button[1]'
#
time.sleep(5)
ul_listings = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul')
all_listings = ul_listings.find_elements(By.CLASS_NAME, value="job-card-container")

for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        element = driver.find_element(By.XPATH,value='/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[6]/div/div/div/button')
        element.click()
        time.sleep(2)
        try:
         submit = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div/form/footer/div[3]/button')
         submit.click()
         done = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/div[3]/button")
         done.click()
        except Exception:
            cancel = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/button')
            cancel.click()
            discard = driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div[3]/button[1]')
            discard.click()
    except Exception:
        print("Error")