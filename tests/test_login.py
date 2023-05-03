import time

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.disk_page import DiskPage
from const.const import *

login = LoginPage()
main_page = MainPage()
disk_page = DiskPage()

def test_login():
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

    # try:
    #     assert login.get_title_text_after_password() == \
    #            "Добавьте почту. Если потеряете доступ к своему аккаунту, " \
    #            "его можно будет проще восстановить с её помощью.", "Page name has changed, " \
    #                                                                           "or foreign localization"
    #     login.click_skip_button()
    # except Exception as E:
    #     print(E)

    assert login.get_title_text_after_password() == "Войдите, чтобы продолжить", "Page name has changed, " \
                                                                              "or foreign localization"
    time.sleep(3)


# def test_disk():
    main_page.open_disk()
    disk_page.click_create_button()
    disk_page.click_create_folder_button()
    time.sleep(2)
    print(disk_page.get_text_from_dialog_title())
    disk_page.type_title_of_folder()
    disk_page.click_button_save()
    time.sleep(3)
    disk_page.remove_selection()
    time.sleep(2)
    disk_page.double_click_on_new_folder()
    time.sleep(2)

    assert disk_page.get_title_of_new_folder() == TITLE_FOLDER

    disk_page.click_create_button()
    disk_page.click_create_file()
    print(disk_page.get_text_from_dialog_title())
    disk_page.type_title_of_file()
    disk_page.click_button_save()
    time.sleep(2)
    disk_page.close_tab_of_file()

    assert disk_page.get_title_of_new_file() == TITLE_FILE + ".docx"

    time.sleep(10)



