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
    # driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.truenorthdestinations.ca/book")
    driver.implicitly_wait(3)

    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(3)

    check_in = driver.find_element(By.NAME, "search_start_date")
    check_in.click()

    try:
        found = driver.find_element(By.XPATH, "//div[contains(@class, 'css-ocg6bg') and .//div[contains(@class, '2024-08')] and .//div[@class='day default']/p[text()='29'] and .//div[@class='day default']/div[@class='dot']]")
    except NoSuchElementException:
        found = None
    try:
        not_found = driver.find_element(By.XPATH, "//div[contains(@class, 'css-ocg6bg') and .//div[contains(@class, '2024-08')] and .//div[@class='day default disabled']/p[text()='29']]")
    except NoSuchElementException:
        not_found = None

    if not_found and not found:
        print(f"{RED}ROOM NOT AVAILABLE{RESET}")
    elif found and not not_found:
        print(f"{GREEN}ROOM AVAILABLE{RESET}")
        send_email()
    else:
        print("found", found)
        print("not_found", not_found)
        print(f"{YELLOW}STATUS UNKNOWN{RESET}")

    driver.quit()

    # Run every 10 minutes
    time.sleep(600)