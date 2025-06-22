from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME,"fName")
fName.send_keys("Parin")

lName = driver.find_element(By.NAME,"lName")
lName.send_keys("Batman")

email = driver.find_element(By.NAME,"email")
email.send_keys("Batman@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

# driver.quit()
