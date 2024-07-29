import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

while True:
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.truenorthdestinations.ca/book")
        driver.implicitly_wait(3)

        iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(3)

        check_in = driver.find_element(By.NAME, "search_start_date")
        check_in.click()

        try:
            not_found = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'day') and contains(@class, 'default') and contains(@class, 'disabled')]/p[text()='29']"))
            )
        except TimeoutException:
            not_found = False

        try:
            found = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'day') and contains(@class, 'default')]/p[text()='29']/following-sibling::div[contains(@class, 'dot')]"))
            )
        except TimeoutException:
            found = False

        if not_found and not found:
            print("NO ROOM AVAILABLE")
        elif found and not not_found:
            print("ROOM AVAILABLE")
        else:
            print("STATUS UNKNOWN")

    finally:
        driver.quit()

    # Run every 10 minutes
    time.sleep(600)