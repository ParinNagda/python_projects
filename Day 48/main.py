from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/OnePlus-Wireless-Earbuds-Drivers-Playback/dp/B0C8JB3G5W/ref=sr_1_2?crid=3LV0W43571LZJ&dib=eyJ2IjoiMSJ9.-eWgZyQULGozbjogKFKF7TbZYljnRytZL8Pjtk6rb965uTALrrgWAXO8WwSp9sIHOwv2Le2NQkIzOa7dCDbVnEKY_lvX2wZfoda-CaYVJMoNkht7E5i8C9J7Prqo2hHZwZyiDlewd-BMQpNxmYhRBTaN_oDN7UHq3dGQh6qX71KLmiYNQods7khQBV7sgw6x1G2P93oklWsDVlaOzxG0h5ZPP1z7lbzOpBCANv_mszo.7jVfST8NPVWrjTcoE-q9lufZ7qruBZBWwiKT7dg9yLI&dib_tag=se&keywords=ear%2Bbuds%2Bwireless&qid=1750398784&sprefix=ear%2Caps%2C466&sr=8-2&th=1")
element = []
try:
    element = driver.find_element(By.CLASS_NAME, "a-price-whole")
except:
    button = driver.find_element(By.CLASS_NAME,"a-button-text")
    button.click()
    element = driver.find_element(By.CLASS_NAME, "a-price-whole")

print(element.text)

driver.quit()