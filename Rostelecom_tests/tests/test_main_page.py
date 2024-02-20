import re

import pytest
from playwright.sync_api import expect

from pages.page_objects.main_page import MainPage

expect.set_options(timeout=10000)


def test_register(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.REGISTER_LINK.click()
    main_page.fill_register_form()
    main_page.locators.REGISTER_BUTTON.click()
    expect(main_page.page).to_have_url(
        re.compile(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration.+'))


@pytest.mark.parametrize('tab_name,user_id',
                         [('PHONE_TAB', '89519509832'), ('MAIL_TAB', 'allyouneedislove242@gmail.com'),
                          ('LOGIN_TAB', 'admin'), ('SELF_ACCOUNT_TAB', '123459876519')])
def test_login(main_page: MainPage, tab_name, user_id) -> None:
    main_page.load()
    main_page.fill_login_form(tab_name, user_id)
    main_page.locators.LOGIN_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://b2c.passport.rt.ru/account_b2c/page.+'))


@pytest.mark.parametrize('tab,user',
                         [('PHONE_TAB', '89519509832'), ('MAIL_TAB', 'allyouneedislove242@gmail.com'),
                          ('LOGIN_TAB', 'admin'), ('SELF_ACCOUNT_TAB', '123459876519')])
def test_restore_password(main_page: MainPage, tab, user) -> None:
    main_page.load()
    main_page.locators.FORGOT_PASSWORD.click()
    main_page.fill_restore_password(tab, user)
    main_page.locators.CONTINUE_BUTTON.click()
    expect(main_page.page).to_have_url(
        re.compile(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate.+'))


def test_help_button(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.HELP_BUTTON.click()
    expect(main_page.locators.HELP_HEADER).is_visible()


def terms_of_use_button(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.TERMS_OF_USE_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'))


def test_mobile_number_with_less_digits(main_page: MainPage, tab_name) -> None:
    main_page.load()
    main_page.locators.PHONE_TAB.click()
    main_page.fill_incorrect_digits(tab_name)
    main_page.locators.LOGIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_NUMBER).is_visible()


def test_password_with_less_digits(main_page: MainPage, tab_name) -> None:
    main_page.load()
    main_page.locators.PHONE_TAB.click()
    main_page.fill_incorrect_password(tab_name)
    main_page.locators.LOGIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGINPASSWORD).is_visible()


def test_incorrect_email(main_page: MainPage, tab_name) -> None:
    main_page.load()
    main_page.locators.MAIL_TAB.click()
    main_page.fill_incorrect_email(tab_name)
    main_page.locators.LOGIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGINPASSWORD).is_visible()


def test_incorrect_login(main_page: MainPage, tab_name) -> None:
    main_page.load()
    main_page.locators.LOGIN_TAB.click()
    main_page.fill_incorrect_login(tab_name)
    main_page.locators.LOGIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGINPASSWORD).is_visible()


def test_self_account_with_less_digits(main_page: MainPage, tab_name) -> None:
    main_page.load()
    main_page.locators.SELF_ACCOUNT_TAB.click()
    main_page.fill_less_digits(tab_name)
    main_page.locators.LOGIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGINPASSWORD).is_visible()


def test_login_with_vk(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.SUPPORT_NUMBER_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://id.vk.com/auth?return_auth_hash=10fe256621a69e3ed4&redirect_uri=https%3A%2F%2Fb2c.passport.rt.ru.+'))


def test_login_with_ok(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.LOGIN_WITH_OK_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://connect.ok.ru/dk?st.cmd=OAuth2Login&st.redirect=%252Fdk%253Fst.cmd.+'))


def test_login_with_mail(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.LOGIN_WITH_MAIL_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://connect.mail.ru/oauth/authorize?scope=login%3Aemail&state=lDai2C2eA8sVs2iDeBQiVRZINei9q5zGqkPYB20Nn-Y.iN8-wjxrhMk.account_b2c&response_type=code&client_id=762573.+'))


def test_login_with_yandex(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.LOGIN_WITH_YANDEX_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://oauth.yandex.ru/authorize?scope=login%3Aemail&state=mZPPQ6v553lDyBNittT_J47G0xMSlLk252q3unPvsPs.69J5odOFJGk.account_b2c&response_type=code&client_id=cca955e781554be08e4007813ddd578e.+'))


def test_cookies_definition(main_page: MainPage) -> None:
    main_page.load()
    main_page.locators.COOKIES_BUTTON.click()
    expect(main_page.locators.COOKIES_USE).is_visible()
