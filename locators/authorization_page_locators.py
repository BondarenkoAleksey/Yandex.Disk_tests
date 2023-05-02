from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN_INPUT = (By.ID, 'passp-field-login')
    PASSWORD_INPUT = (By.ID, 'passp-field-passwd')
    LOGIN_BUTTON = (By.ID, 'passp:sign-in')

    TITLE_AFTER_LOGIN = (By.CLASS_NAME, "WelcomePage-tagline")
    TITLE_AFTER_PASS = (By.CLASS_NAME, "passp-title")

    SKIP_BUTTON = (By.CSS_SELECTOR, 'button[data-t="button:pseudo"]')
