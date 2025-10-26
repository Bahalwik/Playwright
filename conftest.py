import pytest
from playwright.sync_api import Playwright, sync_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture()
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {

        "viewport": {

            "width": 1000,

            "height": 1000,

        }

    }


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

