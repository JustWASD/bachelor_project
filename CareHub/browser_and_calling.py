#Standard
import time
import cfg

#Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


connected = 0

#opens a browser window and hides it via the "wait_for_connect_window"
#closes the "wait_for_connect_window" if a call was successfully established
#or turns the windows red if it failed.
def start_call():
    
    chrome_options = Options()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--kiosk")
    chrome_options.add_argument("use-fake-ui-for-media-stream")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(cfg.url)

    time.sleep(4)
    login = driver.find_element(By.CLASS_NAME, 'field  ')
    driver.find_element(By.CLASS_NAME, 'chrome-extension-banner__close-container').click()

    # logs in
    login.send_keys("CareHub")
    login.send_keys(Keys.RETURN)

    # wait 2min30secs for second person to join the call
    try:
        WebDriverWait(driver, 150).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'stage-participant-label')))
        cfg.call_connected = 1
    except:
        cfg.call_connected = 0
        print("timed out!")

    if cfg.call_connected == 1:
        print("connected")
        cfg.wait_for_connect_window.destroy()
        
        while True:
            try:
                WebDriverWait(driver, 3).until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME, 'stage-participant-label')))
            except:
                print("call ended")
                driver.close()
                cfg.call_connected = 0
                break
            time.sleep(5)
    else:
        print("no connection established")
        cfg.wait_for_connect_window.config(bg="red")
        driver.close()
        #20 seconds of error message
        time.sleep(20)
        cfg.wait_for_connect_window.destroy()
        return 2

