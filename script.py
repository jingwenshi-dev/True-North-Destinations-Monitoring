import time
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def send_email():
    sender = "jingwensteven.shi@gmail.com"
    password = ""
    recipients = [sender]

    msg = MIMEText("https://www.truenorthdestinations.ca/book")
    msg['Subject'] = "泡泡屋有空房啦！"
    msg['From'] = "jingwensteven.shi@gmail.com"
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

    print("Message sent!")


while True:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)

        driver.get("https://www.truenorthdestinations.ca/book")
        driver.implicitly_wait(3)

        iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(3)

        print("Finding room availability...")

        check_in = driver.find_element(By.XPATH, "//button[@data-testid='landing-search-panel-date-picker-checkin-input']")
        check_in.click()
        driver.implicitly_wait(3)

        room_available = None

        try:
            august_month = driver.find_element(By.XPATH, "//div[@data-testid='calendar-month-august']")
        except NoSuchElementException:
            august_month = None

        if august_month:
            try:
                room_available = august_month.find_element(By.XPATH,".//div[@data-testid='day-2024-08-27-restrictions-indicator']")
            except NoSuchElementException:
                room_available = False

        if room_available:
            print(f"{GREEN}ROOM AVAILABLE{RESET}")
            send_email()
        elif room_available is None:
            print(f"{YELLOW}ROOM AVAILABILITY UNKNOWN{RESET}")
        else:
            print(f"{RED}ROOM NOT AVAILABLE{RESET}")

        driver.quit()

        # Run every 10 minutes
        time.sleep(60)

    except Exception as e:
        pass
