from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts.futbolkolektyw.pl/en/')
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    remind_password_xpath = "//h5[(text()= 'Remind password')]"
    sendemail_field_xpath = "//*[(@name='email')]"
    send_button_xpath = "//span[text()= 'Send']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_the_remind_password_button(self):
        self.click_on_the_element(self.remind_password_xpath)

    def type_in_sendemail(self, sendemail):
        self.field_send_keys(self.sendemail_field_xpath, sendemail)

    def click_on_the_send_button(self):
        self.click_on_the_element(self.send_button_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title