from utils import date_time_manager as dt
from services import get_users
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time





if __name__== "__main__":
    CHROME_PATH = "F:\Python\InstaBot\\resources\chromedriver_win32\chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()
    capabilities = {
        'browserName': 'chrome',
        'chromeOptions': {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--start-maximized', '--disable-infobars']
        }
    }

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_PATH,
                              desired_capabilities=capabilities)

    user_getter = get_users.GetUsers(driver)
    user_getter.run()
    # user_getter.login()
    # user_getter.get_followers_from_user("sofiavergara")