from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import signal

signal.alarm(720)

now = datetime.datetime.now()

current_time = now.strftime("%H:%M / %A")


justtime = now.strftime("%H:%M")


op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-user")

driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options= op)

driver.get("https://youtube.com")
print(driver.page_source)
