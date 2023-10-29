import allure
import pytest
from page_objects.AdminLoginPage import LoginAsAdmin
import time
from page_objects.BasePage import BasePage
from page_objects.AdminPage import AdminPage
from page_objects.RegistryPage import RegistryPage
from page_objects.MainPage import MainPage
from helpers import generate_random_user
from helpers import random_product

TEST_PATTERN = '_test_'


@allure.epic("OPENCART")
@allure.title('Регистрация пользователя')
@pytest.mark.parametrize("i", range(2))
def test_reg_user(browser, i):
    reg_page = RegistryPage(browser)
    reg_page.click_register()
    user_data = generate_random_user()
    reg_page.register_user(user_data)
    time.sleep(0.1)
    try:
        assert "Your Account Has Been Created!" in browser.page_source
    except AssertionError:
        BasePage(browser).capture_screenshot()
        raise AssertionError('TEST FAILD')


@allure.epic("OPENCART")
@allure.title('Проверка авторизации с ложным пользователем')
@pytest.mark.parametrize("login", ["Gorge", "admin"])
@pytest.mark.parametrize("password", ['qweASSD', 'ASDFQWE'])
def test_wrong_admin_logging(browser, login, password):
    browser.get(browser.current_url + 'admin/')
    loging_page = LoginAsAdmin(browser)
    loging_page.log_as_admin(login, password)
    try:
        assert BasePage.alert_wait is not None
    except AssertionError:
        BasePage(browser).capture_screenshot()
        raise AssertionError('TEST FAILD')


@pytest.fixture(scope='function')
def admin_login(browser, admin_password, admin_login):
    browser.get(browser.current_url + 'admin/')
    login_page = LoginAsAdmin(browser)
    login_page.log_as_admin(admin_login, admin_password)


@allure.epic("OPENCART")
@allure.title('Добавление продукта в магазин')
@pytest.mark.parametrize("i", range(1))
def test_add_product(browser, admin_login, i):
    admin_page = AdminPage(browser)
    product_data = random_product(TEST_PATTERN)
    admin_page.add_product(product_data)
    try:
        assert TEST_PATTERN in admin_page.name_of_first_product()
    except AssertionError:
        BasePage(browser).capture_screenshot()
        raise AssertionError('TEST FAILD')
    admin_page.delete_test_prod(TEST_PATTERN)


@allure.epic("OPENCART")
@allure.title('Проверка удаления продукта из магазина')
@pytest.mark.parametrize("i", range(1))
def test_del_product(browser, admin_login, i):
    admin_page = AdminPage(browser)
    product_data = random_product(TEST_PATTERN)
    admin_page.add_product(product_data)
    admin_page.delete_test_prod(TEST_PATTERN)
    time.sleep(0.5)
    try:
        assert TEST_PATTERN not in admin_page.name_of_first_product()
    except AssertionError:
        BasePage(browser).capture_screenshot()
        raise AssertionError('TEST FAILD')


@allure.epic("OPENCART")
@allure.title('Проверка смены валюты')
@pytest.mark.parametrize("currency", ["gbp", "eur", "usd"])
def test_of_currency_btn(browser, currency):
    main_page = MainPage(browser)
    main_page.chose_currency(currency)
    try:
        assert main_page.actual_currency_symbol() in main_page.get_first_product_price()
    except AssertionError:
        BasePage(browser).capture_screenshot()
        raise AssertionError('TEST FAILD')


@allure.epic("OPENCART")
@allure.title('Ломанный тест')
def test_failure_test(browser):
    reg_page = RegistryPage(browser)
    reg_page.click_register()
    user_data = generate_random_user()
    reg_page.register_user(user_data)
    time.sleep(0.1)
    try:
        assert "FAILD TIME" in browser.page_source
    except AssertionError:
        BasePage(browser).capture_screenshot()
        raise AssertionError('TEST FAILD')
