from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_heder_text_xpath = "//h6[contains(text(),'Scouts Panel')]"
    main_page_button_xpath = "//span[contains(text(),'Main page')]"
    players_button_xpath = "//span[contains(text(),'Players')]"
    change_language_button_xpath = "//*[@id='__next']//ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//span[contains(text(),'Sign out')]"
    players_count_screen_xpath = "//*[@id='__next']//main/div[2]/div[1]/div"
    matches_count_screen_xpath = "//*[@id='__next']//main/div[2]/div[2]/div"
    reports_count_screen_xpath = "//*[@id='__next']//main/div[2]/div[3]/div"
    events_count_screen_xpath = "//*[@id='__next']//main/div[2]/div[4]/div"
    scouts_panel_logo_xpath = "//*[@id='__next']//main/div[3]/div[1]/div/div[1]"
    add_player_button_xpath = "//*[contains(text(),'Add player')]"
    activity_panel_logo_xpath = "//h2[contains(text(),'Activity')]"
