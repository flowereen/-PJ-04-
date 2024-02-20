from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = 'https://b2c.passport.rt.ru/auth'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = MainPageLocators(page)

    def fill_register_form(self):
        self.locators.FIRST_NAME.type('Анастасия')
        self.locators.LAST_NAME.type('Ельфимова')
        self.locators.MOBILE_NUMBER.type('89519509832')
        self.locators.PASSWORD.type('Qwerty12345')
        self.locators.CONFIRM_PASSWORD.type('Qwerty12345')

    def fill_login_form(self, tab_name, user_id):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME.type(user_id)
        self.locators.PASSWORD.type('Qwerty12345')

    def fill_restore_password(self, tab, user):
        getattr(self.locators, tab).click()
        self.locators.USERNAME.type(user)

    def fill_incorrect_password(self, tab_name):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME.type('8951950983')
        self.locators.PASSWORD.type('Qwerty1')

    def fill_incorrect_digits(self, tab_name):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME.type('8951950983')
        self.locators.PASSWORD.type('Qwerty12345')

    def fill_incorrect_email(self, tab_name):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME.type('youneedlovegmail.com')
        self.locators.PASSWORD.type('Qwerty12345')

    def fill_incorrect_login(self, tab_name):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME.type('a1d2m3i4n5')
        self.locators.PASSWORD.type('Qwerty12345')

    def fill_less_digits(self, tab_name):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME.type('12345987651')
        self.locators.PASSWORD.type('Qwerty12345')
