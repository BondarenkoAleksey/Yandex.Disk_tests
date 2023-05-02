from pages.base_page import *
from locators.main_page_locators import *
from locators.authorization_page_locators import *
from const.login import *

class LoginPage(BasePage):

    def open_yaru(self):
        self.open("https://ya.ru")

    def click_enter_button(self):
        self.click(MainPageLocators.ENTER_BUTTON)

    def get_attribute_of_email_tab(self):
        return self.get_attribute(AuthPageLocators.LOGIN_TAB, "aria-pressed")

    def click_email_tab(self):
        self.click(AuthPageLocators.LOGIN_TAB)

    def type_login(self):
        self.type_text(AuthPageLocators.LOGIN_INPUT, LOGIN)

    def get_text_from_login_input(self):
        return self.get_attribute(AuthPageLocators.LOGIN_INPUT, "value")

    def click_login_button(self):
        self.click(AuthPageLocators.LOGIN_BUTTON)

    def get_title_text_after_login(self):
        return self.get_text(AuthPageLocators.TITLE_AFTER_LOGIN)

    def type_password(self):
        self.type_text(AuthPageLocators.PASSWORD_INPUT, PASSWORD)

    def get_text_from_password_input(self):
        return self.get_attribute(AuthPageLocators.PASSWORD_INPUT, "value")

    def get_title_text_after_password(self):
        return self.get_text(AuthPageLocators.TITLE_AFTER_PASS)

    def click_skip_button(self):
        self.click(AuthPageLocators.SKIP_BUTTON)
