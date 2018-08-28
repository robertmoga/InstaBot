# import database_crawl as dbc
from utils import date_time_manager as dt

from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_PATH = "D:\PythonWorks\Selenium\chromedriver_win32\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
capabilities = {
      'browserName': 'chrome',
      'chromeOptions':  {
        'useAutomationExtension': False,
        'forceDevToolsScreenshot': True,
        'args': ['--start-maximized', '--disable-infobars']
    }
}


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_PATH, desired_capabilities=capabilities)

def get_new_user_names():

    #params : user la care sa caute
    #o sa intoarca o lista de username-uri
    #tratez cazul in care nu merge apasat pe buton
    # xpath : //div[@ class='_1xe_U']/li[@ class='NroHT'][1]/div[@ class='ywte8']/div[@ class='gdFJk']/div[@class='foB1c']/div[@class = 'FsskP']/a

    #undeva o metoda care sabage userii noi in baza de date si sa verifice daca au mai fost procesati.


    driver.get("D:\PythonWorks\InstaBot\\resources\\followers.html")
    try:
        driver.find_element(By.XPATH, "//div[@ id='portlet_windows']/"
                                  "div[@ class='teaser clearfix']/form/ "
                                  "div[@class='button p clearfix']/a").click()
    except Exception as e:
        print("No entitlement needed")



hue()