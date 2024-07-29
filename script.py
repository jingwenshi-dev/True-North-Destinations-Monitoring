from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

check_in_date = "10/27/2024"
check_out_date = "10/29/2024"

driver = webdriver.Chrome()

try:
    driver.get("https://www.truenorthdestinations.ca/book")
    driver.implicitly_wait(3)

    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(3)

    check_in = driver.find_element(By.NAME, "search_start_date")
    check_in.clear()
    check_in.send_keys(check_in_date)
    driver.implicitly_wait(3)

    check_out = driver.find_element(By.NAME, "search_end_date")
    check_out.clear()
    check_out.send_keys(check_out_date)
    driver.implicitly_wait(3)

    print(check_in, check_out)
    time.sleep(5)

    # search_button = driver.find_element(By.NAME, "check_availability")
    # search_button.click()

    # results = driver.find_element(By.CLASS_NAME, "av_roomtype")
    # print(results.text)

finally:
    # Close the WebDriver
    driver.quit()
