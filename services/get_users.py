import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from services import database_crawl as dbc
from utils import date_time_manager as dtm
from utils import db_ops, logger
from models import user


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
        self.user_list = dbc.get_new_users()
        self.driver = driver

    def run(self):
        logger.log("Starting GET USER service")
        self.login()

        logger.log("This session iterates through " + str(len(self.user_list)))
        for item in self.user_list:
            print(">> Get Users : " + str(item) + "\n")
            #getting users from current user
            new_users = self.get_followers_from_user(item.name)

            #modify and update in db for current users
            item.next_action = "follow"
            item.next_date = dtm.get_next_time(False, True)
            db_ops.update_user(item)
            #commit other users to db
            for elem in new_users:
                new_user = user.User(elem)
                db_ops.add_user(new_user)

    def login(self):
        logger.log("Performing login")
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
        logger.log("Log in succeeded")

    def get_followers_from_user(self, curent_usr):

        logger.log("Getting follwers from user " + curent_usr)
        # param - user-ul in lista caruia sa caut
        users_list = list()
        url = "https://www.instagram.com/" + curent_usr + "/followers"
        self.driver.get(url)
        self.driver.find_element(By.XPATH,"//section[@class='zwlfE']/ul/li[2]/a").click()

        try:
            self.driver.find_element(By.XPATH, "//div[@ id='portlet_windows']/"
                                               "div[@ class='teaser clearfix']/form/ "
                                               "div[@class='button p clearfix']/a").click()
        except Exception as e:
            print("No entitlement needed")
        time.sleep(2)
        try:
            for i in range(1, 5):
                temp = self.driver.find_element_by_xpath("//div[@ class='j6cq2']/ul/div/li["+str(i)+"]/div/div/div[2]/div/a").text
                users_list.append(temp)
                # print(temp)
        except Exception as e:
            print("Error in retriving followers" + str(e))
        logger.log("Returning " + str(len(users_list)) + "users from " + curent_usr)
        return users_list
