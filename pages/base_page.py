import time

import pyautogui as pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

class BasePage:

    def open(self, url):
        driver.get(url)

    def find_element(self, locator, time=25):
        wait = WebDriverWait(driver, time)
        return wait.until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, by, value):
        return self.find_elements(by, value)

    def page_title(self):
        return driver.title

    def click(self, locator):
        self.find_element(locator).click()

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        # actions = ActionChains(driver)
        # actions.send_keys()
        element.send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        element.send_keys(Keys.BACKSPACE*20)
        # element.clear()
        element.send_keys(text)


    def get_attribute(self, locator, key):
        element = self.find_element(locator)
        return element.get_attribute(key)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_present(self, how, what):
        try:
            driver.find_element(how, what)
        except NoSuchElementException:
            print(f"Element {driver.find_element(how, what)} not found")
            return False
        return True

    def page_reload(self):
        driver.refresh()

    def execute_script(self, value):
        return driver.execute_script(value)

    def click2(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def find_element2(self, how, what, time=25):
        wait = WebDriverWait(driver, time)
        return wait.until(EC.presence_of_element_located((how, what)), message=f"Can't find element by locator {locator}")

    def double_click(self,locator):
        element = self.find_element(locator)
        actions = ActionChains(driver)
        return actions.double_click(element).perform()

    def send_keys_keyboard(self, locator, key):
        ActionChains(driver).move_to_element(locator).key_down(key).key_up(key).perform()

    def close_tab(self):
        pyautogui.keyDown('command')
        pyautogui.press('w')
        pyautogui.keyUp('command')

    def switch_tab(self, handle):
        driver.switch_to.window(driver.window_handles[handle])