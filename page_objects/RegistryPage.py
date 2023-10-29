from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class RegistryPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    E_MAIL = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#input-confirm')
    ACCOUNT_BTN = (By.CSS_SELECTOR, 'a.dropdown-toggle[title="My Account"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'ul.dropdown-menu li:first-child a')
    AGREEMENT_FOR_PP = (By.XPATH, '//input[@name="agree"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'input[value="Continue"]')

    @allure.step("Перехожу на страницу регистрации")
    def click_register(self):
        self.click(RegistryPage.ACCOUNT_BTN)
        self.click(RegistryPage.REGISTER_BTN)

    def fill_fake_user(self, user_data):
        self.fill_strings(self.FIRST_NAME, user_data['First Name'])
        self.fill_strings(self.LAST_NAME, user_data['Last Name'])
        self.fill_strings(self.E_MAIL, user_data['E-Mail'])
        self.fill_strings(self.TELEPHONE, user_data['Telephone'])
        self.fill_strings(self.PASSWORD, user_data['Password'])
        self.fill_strings(self.CONFIRM_PASSWORD, user_data['Password'])

    @allure.step("Заполняю данные пользователя и регистрирую его")
    def register_user(self, user_data):
        self.fill_fake_user(user_data)
        self.click(self.AGREEMENT_FOR_PP)
        self.click(self.CONTINUE_BTN)
