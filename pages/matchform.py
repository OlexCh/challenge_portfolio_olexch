from pages.base_page import BasePage


class MatchForm(BasePage):
    adding_match_player_page_logo_xpath = "//*[@id='__next']//form/div[1]/div/span"
    my_team_field_xpath = "//*[@id='__next']//form/div[2]//div[1]/div/div/input"
    enemy_team_field_xpath = "//*[@id='__next']//form/div[2]//div[2]/div/div/input"
    my_team_score_field_xpath = "//*[@id='__next']//form/div[2]//div[3]/div/div/input"
    enemy_team_score_field_xpath = "//*[@id='__next']//form/div[2]//div[4]/div/div/input"
    date_field_xpath = "//input[@name='date']"
    t_shirt_color_field_xpath = "//input[@name='tshirt']"
    league_field_xpath = "//input[@name='league']"
    time_played_field_xpath = "//input[@name='timePlayed']"
    web_match_field_xpath = "//input[@name='webMatch']"
