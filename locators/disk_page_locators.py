from selenium.webdriver.common.by import By


class DiskPageLocators:
    BUTTON_CREATE = 'return document.querySelector("button[class=\'Button2 Button2_view_raised ' \
                    'Button2_size_m Button2_width_max\']").click()'
    BUTTON_CREATE_FOLDER = 'return document.querySelector("button[aria-label=\'Папку\']").click()'
    DIALOG_TITLE = (By.CLASS_NAME, "dialog__title")
    FOLDER_TITLE_INPUT = (By.CSS_SELECTOR, "span.Textinput_view_default .Textinput-Control")
    BUTTON_SAVE = (By.CSS_SELECTOR, ".confirmation-dialog__button.confirmation-dialog__button_submit")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Отменить выделение']")
    FOLDER_BUTTON = (By.XPATH, "(//div[@class='listing-item__fields'])[1]")
    TITLE_OF_NEW_FOLDER = (By.CLASS_NAME, "listing-heading__title-inner")
    BUTTON_CREATE_FILE = 'return document.querySelector("button[aria-label=\'Текстовый документ\']").click()'
    FILE_TITLE_INPUT = (By.CSS_SELECTOR, "input[value='Новый документ']")
    DOCUMENT_BUTTON = (By.XPATH, "(//div[@class='listing-item__fields'])[1]")
    TITLE_OF_NEW_FILE = (By.CSS_SELECTOR, ".clamped-text")
    BACK_BUTTON = (By.XPATH, "(//button[@id='/disk'])[1]")
    AVA_ICON = (By.CSS_SELECTOR, "a[aria-label='Аккаунт'] img[class='user-pic__image']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Выйти из аккаунта'] span[class='menu__text']")