import time

from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    addplayerform_url = 'https://scouts.futbolkolektyw.pl/en/players/add'
    expected_title = "Add player"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    right_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    age_field_xpath = "//*[@name='age']"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    second_position_field_xpath = "//*[@name='secondPosition']"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    lublin_var_xpath = "//*[@id='menu-district']/div[3]/ul/li[3]"
    lubusz_var_xpath = "//*[@id='menu-district']/div[3]/ul/li[4]"
    achievements_field_xpath = "//*[@name='achievements']"
    add_language_button_xpath = "//*[text()='Add language']"
    native_language_field_xpath = "//*[@id='__next']//div[15]/div/div/div/input"
    submit_button_xpath = "//*[text()='Submit']"
    clear_button_xpath = "//*[text()='Clear']"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.addplayerform_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)


    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == 'Left':
            self.click_on_the_element(self.left_leg_xpath)
        else:
            self.click_on_the_element(self.right_leg_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def select_district(self, district):
        self.click_on_the_element(self.district_dropdown_xpath)
        if district == 'lubelskie':
            self.click_on_the_element(self.lublin_var_xpath)
        else:
            self.click_on_the_element(self.lubusz_var_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def click_on_the_add_language_button(self):
        self.click_on_the_element(self.add_language_button_xpath)

    def type_in_native_language(self, native_language):
        self.field_send_keys(self.native_language_field_xpath, native_language)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)