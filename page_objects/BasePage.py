from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

BASE_TIME_WAIT = 5


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self):
        screenshot_named = self.driver.current_url[:35]
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=screenshot_named, attachment_type=allure.attachment_type.PNG)

    @allure.step
    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            element.click()
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError(f"Element {locator} not clickable within {BASE_TIME_WAIT} seconds.")

    @allure.step
    def fill_strings(self, locator, data):
        try:
            element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.element_to_be_clickable(locator))
            self.click(locator)
            ActionChains(self.driver).pause(0.2).click(element).send_keys(data).perform()
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError(f"Cant fill the string {locator}")

    @allure.step
    def wait_for_element(self, locator, timeout=BASE_TIME_WAIT):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError(f"Element {locator} not found within {timeout} seconds.")

    @allure.step
    def get_text(self, locator):
        try:
            element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError(f'Cant find text in {locator}')

    @allure.step
    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError(f'Cant find element {locator}')

    @allure.step
    def find_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError(f'Cant find elements in {locator}')

    @allure.step
    def alert_wait(self):
        try:
            alert = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.alert_is_present())
            return alert
        except TimeoutException:
            self.capture_screenshot()
            raise TimeoutError('No alert')
