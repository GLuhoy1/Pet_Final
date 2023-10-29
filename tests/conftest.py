import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--headless", default="headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.1.68:8081/")
    parser.addoption("--admin_login", default='*****')
    parser.addoption("--admin_password", default='******')


@pytest.fixture()
def browser(request):
    headless = request.config.getoption("--headless")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get(request.config.getoption("--base_url"))
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def admin_password(request):
    return request.config.getoption("--admin_password")


@pytest.fixture(scope='function')
def admin_login(request):
    return request.config.getoption("--admin_login")
