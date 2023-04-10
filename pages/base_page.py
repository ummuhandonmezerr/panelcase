import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.hover = ActionChains(self.driver)
        self.test_number = random.randint(0, 1000000)

    def element_located(self, *locator):
        return self.wait.until(ec.presence_of_element_located(*locator))

    def all_elements_located(self, *locator):
        return self.wait.until(ec.presence_of_all_elements_located(*locator))

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, index, *element):
        return self.driver.find_elements(*element)[index]

    def send_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

        return self

    def click_element(self, *locator):
        self.find_element(*locator).click()

        return self

    def visibility_of_element(self, *locator):
        return self.wait.until(ec.visibility_of_element_located(*locator))

    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def hover_move_to_element(self, *locator):
        return self.hover.move_to_element(*locator).perform()

    def scroll_execute_script(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_element_clickable(self, locator, message=""):
        return self.wait.until(ec.element_to_be_clickable(locator), message)

    def click(self, *locator):
        self.find_element(*locator).click()

    def fill(self, text, *locator):
        self.find_element(*locator).send_keys(text)

        return self

    def switch_frame(self, locator):
        return self.SwitchFrame(self.driver, self.wait_for_element_clickable(locator))

    class SwitchFrame:
        def __init__(self, driver, element):
            self.driver = driver
            self.element = element