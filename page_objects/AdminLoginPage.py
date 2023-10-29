from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class LoginAsAdmin(BasePage):
    USERNAME_STRING = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_STRING = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")

    @allure.step("Логаюсь как админ")
    def log_as_admin(self, login, password):
        self.fill_strings(self.USERNAME_STRING, login)
        self.fill_strings(self.PASSWORD_STRING, password)
        self.click(self.LOGIN_BUTTON)
