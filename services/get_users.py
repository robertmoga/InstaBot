import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from services import database_crawl as dbc
from utils import date_time_manager as dtm
from utils import db_ops

# CHROME_PATH = "F:\Python\InstaBot\\resources\chromedriver_win32\chromedriver.exe"
#
# chrome_options = webdriver.ChromeOptions()
# capabilities = {
#     'browserName': 'chrome',
#     'chromeOptions': {
#         'useAutomationExtension': False,
#         'forceDevToolsScreenshot': True,
#         'args': ['--start-maximized', '--disable-infobars']
#     }
# }
#
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_PATH,
#                               desired_capabilities=capabilities)
#
#

class GetUsers:

    def __init__(self, driver):
        self.user_list = dbc.get_users_profile_crawling()
        self.driver = driver

    def run(self):
        self.login()

        for item in self.user_list:
            print(">> Get Users : " + str(item) + "\n")
            #getting users from current user
            new_users = self.get_users_by_user(item.name)

            #modify and update in db for current users
            item.next_action = "follow"
            item.next_date = dtm.get_next_time(False, True)
            db_ops.update_user(item)
            #commit other users to db
            print(new_users)

    def login(self):

        credentials = ['test.dev.ro01@gmail.com', 'TestPass01']
        self.driver.get("https://www.instagram.com/accounts/login/")
        try:
            wait = WebDriverWait(self.driver, 2)
            element = wait.until(EC.presence_of_element_located((By.ID, 'f38b11295d06a08')))
        except:
            print("Error at wait")

            self.driver.find_element_by_xpath("//form[@class='HmktE']/div[1]/div/div/input").send_keys(credentials[0])
            self.driver.find_element_by_xpath("//form[@class='HmktE']/div[2]/div/div/input").send_keys(credentials[1])

            self.driver.find_element_by_xpath("//form[@class='HmktE']/span/button").click()

        time.sleep(2)  # wait
        self.driver.find_element_by_xpath("//a[@href='/']").click()

    def get_users_by_user(self, curent_usr):

        # param - user-ul in lista caruia sa caut
        users_list = list()
        url = "https://www.instagram.com/" + curent_usr + "/followers"
        self.driver.get(url)
        try:
            self.driver.find_element(By.XPATH, "//div[@ id='portlet_windows']/"
                                               "div[@ class='teaser clearfix']/form/ "
                                               "div[@class='button p clearfix']/a").click()
        except Exception as e:
            print("No entitlement needed")

        try:
            for i in range(1, 10):
                temp = self.driver.find_element_by_xpath("//div[@ class='_1xe_U']/li[@ class='NroHT'][" + str(
                    i) + "]/div[@ class='ywte8']/div[@ class='gdFJk']/div[@class='foB1c']/div[@class = 'FsskP']/a").text
                users_list.append(temp)
        except Exception as e:
            print("Error in retriving followers" + str(e))

        return users_list
