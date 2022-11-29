import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service



from selenium import webdriver

from pages.add_new_player_form import AddPlayerForm
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(3)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(4)
        dashboard_page.click_on_add_player_button()
        dashboard_page.form_title_of_page()
        time.sleep(3)
        add_player = AddPlayerForm(self.driver)
        add_player.title_of_page()
        add_player.type_in_email('zinedin@zidan.com')
        add_player.type_in_name('Zinedin')
        add_player.type_in_surname('Zidane')
        add_player.type_in_phone('222333222')
        add_player.type_in_weight('83')
        add_player.type_in_height('185')
        add_player.type_in_age('23061972')
        add_player.select_leg('Left')
        time.sleep(4)
        add_player.type_in_club('Real Madrid')
        add_player.type_in_level('Premium')
        add_player.type_in_main_position('')
        add_player.type_in_second_position('midfielder')
        add_player.select_district('lubelskie')
        add_player.type_in_achievements('Greatest Soccer of All Time')
        time.sleep(4)
        add_player.click_on_the_add_language_button()
        time.sleep(5)
        add_player.type_in_native_language('French')
        time.sleep(5)
        add_player.click_on_the_clear_button()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()