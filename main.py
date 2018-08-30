from utils import date_time_manager as dt
from services import profile_crawling as pc
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_PATH,
    #                           desired_capabilities=capabilities)

    pc.login()
