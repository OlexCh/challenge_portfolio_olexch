import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_button_xpath = "//*[text()='Add player']"
    expected_form = 'Add player'
    addplayerbutton_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'


    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def form_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.addplayerbutton_url) == self.expected_form
