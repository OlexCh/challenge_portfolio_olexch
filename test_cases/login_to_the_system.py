import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service



from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() #check if the title of the oprned page is correct
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    def test_password_recovery(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check if the title of the opened page is correct
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('rtgws')
        user_login.click_on_the_sign_in_button()
        time.sleep(4)
        user_login.click_on_the_remind_password_button()
        time.sleep(3)
        user_login.type_in_sendemail('test')
        user_login.click_on_the_send_button()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()