
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
    


chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_argument("--start-fullscreen");
chrome_options.add_argument("--kiosk");
chrome_options.add_argument("use-fake-ui-for-media-stream")

# executable_path=("/usr/lib/chromium-browser/chromium-browser")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://meet.jit.si/ClinicalMirrorsHandleConsistently")

time.sleep(10)
login = driver.find_element(By.CLASS_NAME, 'field  ')

login.send_keys("pycon")
login.send_keys(Keys.RETURN)


time.sleep(30)


driver.close()