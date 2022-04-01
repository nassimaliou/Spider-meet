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


op = Options()

#op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

op.add_argument("--disable-infobars")
op.add_argument("start-maximized")
op.add_argument("--disable-extensions")

"""
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-user")
"""

op.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1,
})



driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options= op)

driver.get("https://youtube.com")
print(driver.page_source)
