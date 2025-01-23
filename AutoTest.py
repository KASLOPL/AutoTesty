from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from imap_tools import MailBox
from Data import data

# Konfiguracja Selenium
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.getresponse.com/")

# Logowanie za pomocą Selenium
driver.find_element(By.CLASS_NAME, "Header_loginButton__WkWFO").click()
sleep(2)
driver.find_element(By.NAME, "email").send_keys(data("email"))
driver.find_element(By.ID, "password").send_keys(data("account_password"))
sleep(1.5)
driver.find_element(By.CLASS_NAME, "neo-button.btn-primary.btn-large.neo-flex.justify-content-center.align-items-center.neo-box").click()
sleep(3)
with MailBox('imap.fastmail.com').login(data("email"), data("imap_password"), "Inbox") as mb:
    for msg in mb.fetch(limit=1, reverse=True, mark_seen=True):
        dwafa = msg.html[10683:10690]

driver.find_element(By.ID, "verificationCode").send_keys(dwafa)
driver.find_element(By.XPATH, "//submit[1]").click()

sleep(1000)
