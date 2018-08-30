# import database_crawl as dbc
from utils import date_time_manager as dt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def login():
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

    credentials = ['test.dev.ro01@gmail.com', 'TestPass01']
    driver.get("https://www.instagram.com/accounts/login/")
    try:
        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, 'f38b11295d06a08')))
    except :
        print("Error at wait")

        # //div[@class = 'f0n8F ']/input[@id='f2c95053c405c54']
    driver.find_element_by_xpath("//form[@class='HmktE']/div[1]/div/div/input").send_keys(credentials[0])
    driver.find_element_by_xpath("//form[@class='HmktE']/div[2]/div/div/input").send_keys(credentials[1])

    driver.find_element_by_xpath("//form[@class='HmktE']/span/button").click()

    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='/']").click()
    time.sleep(120)


def get_new_user_names(driver):

    user_list = list()
    #params : user la care sa caute
    #o sa intoarca o lista de username-uri
    #tratez cazul in care nu merge apasat pe buton
    # xpath : //div[@ class='_1xe_U']/li[@ class='NroHT'][1]/div[@ class='ywte8']/div[@ class='gdFJk']/div[@class='foB1c']/div[@class = 'FsskP']/a

    #undeva o metoda care sabage userii noi in baza de date si sa verifice daca au mai fost procesati.


    driver.get("https://www.instagram.com/salonanovin/followers")
    try:
        driver.find_element(By.XPATH, "//div[@ id='portlet_windows']/"
                                  "div[@ class='teaser clearfix']/form/ "
                                  "div[@class='button p clearfix']/a").click()
    except Exception as e:
        print("No entitlement needed")

    try:
        for i in range(1, 10):
            temp = driver.find_element_by_xpath("//div[@ class='_1xe_U']/li[@ class='NroHT']["+str(i)+"]/div[@ class='ywte8']/div[@ class='gdFJk']/div[@class='foB1c']/div[@class = 'FsskP']/a").text
            user_list.append(temp)
    except:
        print("Error in retriving followers")

    print(user_list)

# get_new_user_names()