from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, 'a[aria-label="Яндекс"]')
    BURGER_BUTTON = (By.CSS_SELECTOR, ".headline__personal-icon>svg")
    ENTER_BUTTON = (By.CSS_SELECTOR, '[data-statlog="headline.enter"]')
    SEARCH_INPUT = (By.ID, "text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    VOICE_BUTTON = (By.CSS_SELECTOR, 'button[data-action="voice"]')
    CAMERA_BUTTON = (By.CSS_SELECTOR, '.search3__svg_camera')
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'button[title="Очистить поисковый запрос"]')
    WEATHER_ICON = (By.CSS_SELECTOR, "div.informers3__item-icon")
    USD_MOEX = (By.CSS_SELECTOR, 'a[title="USD MOEX"]')
    EUR_MOEX = (By.CSS_SELECTOR, 'a[title="EUR MOEX"]')
    GEO_HOME = (By.CSS_SELECTOR, '[data-statlog="informers.geo"]')
    ALICE_ICON = (By.TAG_NAME, "circle")

    
