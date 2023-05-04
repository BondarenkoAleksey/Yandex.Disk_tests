from pages.base_page import *
from locators.disk_page_locators import *
from const.const import *


class DiskPage(BasePage):

    def click_create_button(self):
        el = self.execute_script(DiskPageLocators.BUTTON_CREATE)

    def click_create_folder_button(self):
        self.execute_script(DiskPageLocators.BUTTON_CREATE_FOLDER)

    def get_text_from_dialog_title(self):
        return self.get_text(DiskPageLocators.DIALOG_TITLE)

    def type_title_of_folder(self):
        self.type_text(DiskPageLocators.FOLDER_TITLE_INPUT, TITLE_FOLDER)

    def click_button_save(self):
        self.click(DiskPageLocators.BUTTON_SAVE)

    def remove_selection(self):
        self.click(DiskPageLocators.CLOSE_BUTTON)

    def double_click_on_new_folder(self):
        self.double_click(DiskPageLocators.FOLDER_BUTTON)

    def get_title_of_new_folder(self):
        return self.get_text(DiskPageLocators.TITLE_OF_NEW_FOLDER)

    def click_create_file(self):
        self.execute_script(DiskPageLocators.BUTTON_CREATE_FILE)

    def type_title_of_file(self):
        self.type_text(DiskPageLocators.FILE_TITLE_INPUT, TITLE_FILE)

    def close_tab_of_file(self):
        time.sleep(8)
        self.close_tab()

    def get_title_of_new_file(self):
        return self.get_text(DiskPageLocators.TITLE_OF_NEW_FILE)

    def logout(self):
        self.click(DiskPageLocators.AVA_ICON)
        self.click(DiskPageLocators.LOGOUT_BUTTON)

    def driver_quit(self):
        driver.quit()

    def delete_test_data(self):
        self.click2(DiskPageLocators.BACK_BUTTON)
        time.sleep(0.5)
        self.click2(DiskPageLocators.FOLDER_BUTTON)
        time.sleep(0.5)
        self.press_key("delete")