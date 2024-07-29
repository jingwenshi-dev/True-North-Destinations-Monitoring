import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def send_email():
    sender = "jingwensteven.shi@gmail.com"
    password = ""
    recipients = [sender, 'huangdankun@gmail.com']

    msg = MIMEText("https://www.truenorthdestinations.ca/book")
    msg['Subject'] = "泡泡屋有空房啦！"
    msg['From'] = "jingwensteven.shi@gmail.com"
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())

    print("Message sent!")

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
            print(f"{RED}ROOM NOT AVAILABLE{RESET}")
        elif found and not not_found:
            print(f"{GREEN}ROOM AVAILABLE{RESET}")
            send_email()
        else:
            print(f"{YELLOW}STATUS UNKNOWN{RESET}")

    finally:
        driver.quit()

    # Run every 5 minutes
    time.sleep(290)