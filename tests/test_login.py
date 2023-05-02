import time
import pytest

from pages.login_page import LoginPage
from const.login import *

def test_login():
    login = LoginPage()
    login.open_yaru()
    time.sleep(2)
    login.click_enter_button()
    assert login.page_title() == "Авторизация", "Page name has changed, or foreign localization"
    print(login.page_title())

    if not login.get_attribute_of_email_tab():
        login.click_email_tab()

    login.type_login()
    assert login.get_text_from_login_input() == LOGIN, "Login not entered or wrong login"

    login.click_login_button()
    time.sleep(2)
    assert login.get_title_text_after_login() == "Войдите, чтобы продолжить", "Page name has changed, " \
                                                                              "or foreign localization"

    login.type_password()
    assert login.get_text_from_password_input() == PASSWORD, "Password not entered or wrong password"

    login.click_login_button()

    # TODO Не воспроизводится показ диалога с добавлением доп. адреса электронной почты

    try:
        assert login.get_title_text_after_password() == \
               "Добавьте почту. Если потеряете доступ к своему аккаунту, " \
               "его можно будет проще восстановить с её помощью.", "Page name has changed, " \
                                                                              "or foreign localization"
        login.click_skip_button()
    except Exception as E:
        print(E)

    assert login.get_title_text_after_password() == "Войдите, чтобы продолжить", "Page name has changed, " \
                                                                              "or foreign localization"

    time.sleep(3)
