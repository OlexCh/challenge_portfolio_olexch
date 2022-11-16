from pages.base_page import BasePage

class AddPlayerPage(BasePage):
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[text()='Submit']"

    add_player_button_xpath = "//*[text()='Add player']"
    addplayerbutton_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = 'Add player'
    title_of_box_xpath = "//span[contains(text(),'Add player')]"
    header_of_box = "Add player"

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.addplayerbutton_url) == self.expected_title