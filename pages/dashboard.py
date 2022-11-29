import time

from lib2to3.pgen2 import driver
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_button_xpath = "//*[@title='Logo Scouts Panel']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_button_xpath = "//*[text()='Add player']"
    expected_form_title_of_page = 'Add player'
    addplayerbutton_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    wait = WebDriverWait(driver, 10)


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def form_title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.addplayerbutton_url) == self.expected_form_title_of_page
