import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.authorization_page_locators import AuthPageLocators
from const.login import *

base_page = BasePage()
base_page.open("https://ya.ru")
time.sleep(2)

elem = base_page.find_element(MainPageLocators.ENTER_BUTTON)
elem.click()

assert base_page.page_title() == "Авторизация"

elem = base_page.find_element(AuthPageLocators.LOGIN_INPUT)
elem.send_keys(LOGIN)
assert elem.get_attribute("value") == LOGIN

# проверить нажата ли вкладка ПОЧТА

base_page.find_element(AuthPageLocators.LOGIN_BUTTON).click()

time.sleep(2)

assert base_page.find_element(AuthPageLocators.TITLE_AFTER_LOGIN).text == "Войдите, чтобы продолжить"

elem = base_page.find_element(AuthPageLocators.PASSWORD_INPUT)
elem.send_keys(PASSWORD)
assert elem.get_attribute("value") == PASSWORD

base_page.find_element(AuthPageLocators.LOGIN_BUTTON).click()

try:
    assert base_page.find_element(AuthPageLocators.TITLE_AFTER_PASS).text == "Добавьте почту. Если потеряете доступ к своему аккаунту, его можно будет проще восстановить с её помощью."
    base_page.find_element(AuthPageLocators.SKIP_BUTTON).click()
except Exception:
    pass

assert base_page.find_element(AuthPageLocators.TITLE_AFTER_PASS).text == "Войдите, чтобы продолжить"

time.sleep(3)
