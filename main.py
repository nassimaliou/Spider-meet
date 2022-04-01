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

while justtime != "09:50" or justtime != "13:50" or justtime != "15:20" or justtime != "16:50" :
    time.sleep(20)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    justtime = now.strftime("%H:%M")
    
    if justtime == "09:50" or justtime == "13:50" or justtime == "15:20" or justtime == "16:50" :
        print("Class is going to start in 10 mins")
        break


def gmail_login():
    driver.get("https://accounts.google.com/ServiceLoginservice=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(10)

    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("####EMAIL ADDRESS HERE####")

    time.sleep(4)

    ######

    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)

    ######

    driver.find_element_by_xpath("//input[@name='password']").send_keys("####your email password here####")

    time.sleep(5)

    ####
    
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)

    



driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options= op)

driver.get("https://youtube.com")
print(driver.page_source)
