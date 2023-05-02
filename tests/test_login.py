import time
import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from locators.authorization_page_locators import AuthPageLocators
from const.login import *

# TODO Написать тексты ошибок в ассертах
def test_login():
    login = LoginPage()
    login.open_yaru()
    time.sleep(2)
    login.click_enter_button()
    assert login.page_title() == "Авторизация"

    login.type_login()
    assert login.get_text_from_login_input() == LOGIN

    # TODO проверить нажата ли вкладка ПОЧТА

    login.click_login_button()
    time.sleep(2)
    assert login.get_title_text_after_login() == "Войдите, чтобы продолжить"

    login.type_password()
    assert login.get_text_from_password_input() == PASSWORD

    login.click_login_button()
    try:
        assert login.get_title_text_after_password() == \
               "Добавьте почту. Если потеряете доступ к своему аккаунту, его можно будет проще восстановить с её помощью."
        login.click_skip_button()
    except Exception:
        pass

    assert login.get_title_text_after_password() == "Войдите, чтобы продолжить"

    time.sleep(3)
