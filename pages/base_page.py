from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class BasePage:

    def open(self, url):
        driver.get(url)

    def find_element(self, locator, time=10):
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
        element.clear()
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

    def find_element_with_js(self, value):
        return driver.execute_script(value)

