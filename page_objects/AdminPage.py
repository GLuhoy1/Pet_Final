import time
import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.common.alert import Alert


class AdminPage(BasePage):
    CATALOG_BUTTON = (By.CSS_SELECTOR, '#menu-catalog')
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, '#menu-catalog li:nth-child(2) > a')
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, '.fa-plus')
    GENERAL_TAB = (By.CSS_SELECTOR, 'a[href="#tab-general"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
    META_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEl_STR = (By.CSS_SELECTOR, '#input-model')
    DELETE_BTN = (By.CSS_SELECTOR, '.btn-danger')
    SAVE_BTN = (By.CSS_SELECTOR, '.fa-save')
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, '.table-bordered tbody tr:nth-child(1) td:nth-child(3)')
    FIRST_PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "table.table-bordered tbody tr:first-child input[type='checkbox']")

    @allure.step("Переключась на страницу прдуктов")
    def switch_to_products(self):
        self.click(self.CATALOG_BUTTON)
        self.click(self.PRODUCTS_BUTTON)

    @allure.step("Добавляю тестовый продукт")
    def add_product(self, product_data: dict):
        self.switch_to_products()
        self.click(self.ADD_NEW_BUTTON)
        self.click(self.GENERAL_TAB)
        self.fill_strings(self.PRODUCT_NAME, product_data['product_name'])
        self.fill_strings(self.META_TITLE, product_data['meta_title'])
        self.click(self.DATA_TAB)
        self.fill_strings(self.MODEl_STR, product_data['model'])
        self.click(self.SAVE_BTN)
        self.wait_for_element(self.FIRST_PRODUCT_NAME)

    def name_of_first_product(self):
        return self.get_text(self.FIRST_PRODUCT_NAME)

    @allure.step("Выделяю первый продукт в списке")
    def select_first_test_product(self, test_pattern):
        prod_name = self.name_of_first_product()
        if test_pattern not in prod_name:
            raise ValueError("Not a test generated product")
        else:
            self.click(self.FIRST_PRODUCT_CHECKBOX)

    @allure.step("Удаляю тестовый продукт")
    def delete_test_prod(self, test_pattern):
        self.select_first_test_product(test_pattern)
        self.click(self.DELETE_BTN)
        alert = Alert(self.driver)
        time.sleep(0.1)
        alert.accept()
        time.sleep(0.1)
