from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Update these with your check-in and check-out dates
check_in_date = "10/27/2024"
check_out_date = "10/29/2024"

# Set up the WebDriver (replace 'chromedriver' with the path to your WebDriver if necessary)
driver = webdriver.Chrome()

try:
    driver.get("https://www.truenorthdestinations.ca/book")

    # Wait until the iframe is available and switch to it
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        print(element.get_attribute("name"))

    check_in = driver.find_element(By.NAME, "search_start_date")
    check_in.clear()
    check_in.send_keys(check_in_date)
    check_in.send_keys(Keys.RETURN)

    check_out = driver.find_element(By.NAME, "search_end_date")
    check_out.clear()
    check_out.send_keys(check_out_date)
    check_out.send_keys(Keys.RETURN)


    search_button = driver.find_element(By.NAME, "check_availability")
    search_button.click()

    results = driver.find_element(By.CLASS_NAME, "av_roomtype")
    print(results.text)

finally:
    # Close the WebDriver
    driver.quit()
