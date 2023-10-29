from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class MainPage(BasePage):
    ACCOUNT_BTN = (By.CSS_SELECTOR, 'a.dropdown-toggle[title="My Account"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'ul.dropdown-menu li:first-child a')
    CURRENCY_MENU = (By.CSS_SELECTOR, '.fa-caret-down')
    CURRENCY_EUR = (By.CSS_SELECTOR, '.currency-select[name="EUR"]')
    CURRENCY_GBP = (By.CSS_SELECTOR, '.currency-select[name="GBP"]')
    CURRENCY_USD = (By.CSS_SELECTOR, '.currency-select[name="USD"]')
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, '.product-layout:nth-child(1) .price')
    CURRENCY_SYMBOL = (By.CSS_SELECTOR, '#top .btn-group strong')

    def click_register(self):
        self.click(self.ACCOUNT_BTN)
        self.click(self.REGISTER_BTN)

    @allure.step("Кликаю на кнопку выбора валюты")
    def currency_menu_click(self):
        self.click(self.CURRENCY_MENU)

    @allure.step("Выбираю валюту")
    def chose_currency(self, currency):
        allure.attach(f'Валюта: {currency}', name="Валюта")
        self.currency_menu_click()
        if str(currency).upper() == "USD":
            self.click(self.CURRENCY_USD)
        elif str(currency).upper() == "EUR":
            self.click(self.CURRENCY_EUR)
        elif str(currency).upper() == "GBP":
            self.click(self.CURRENCY_GBP)

    def get_first_product_price(self):
        return self.get_text(self.FIRST_PRODUCT_PRICE)

    def actual_currency_symbol(self):
        return self.get_text(self.CURRENCY_SYMBOL)
