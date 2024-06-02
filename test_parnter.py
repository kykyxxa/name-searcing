import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 2560,
            "height": 1440,
        }
    }


def test_partners(page: Page):
    page.goto('https://guu.ru/')
    page.get_by_role('link', name='Институт информационных систем').click()
    page.get_by_role('link', name='Кафедра информационных систем').click()
    #page.get_by_role('link', name='ПАРТНЕРЫ').click()
    expect(page.get_by_text('ПАРТНЕРЫ')).to_be_visible()

