from pages.base_page import *
from locators.main_page_locators import *
from locators.authorization_page_locators import *
from const.const import *

class MainPage(BasePage):

    def open_disk(self):
        self.open("https://disk.yandex.ru/?source=main-loginmenu/")