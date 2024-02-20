from playwright.sync_api import Page


class MainPageLocators:
    def __init__(self, page: Page):
        self.REGISTER_LINK = page.get_by_role("link", name="Зарегистрироваться")
        self.FIRST_NAME = page.locator("input[name=\"firstName\"]")
        self.LAST_NAME = page.locator("input[name=\"lastName\"]")
        self.REGION = page.locator("input[type=\"text\"]").nth(2)
        self.MOBILE_NUMBER = page.locator("#address")
        self.PASSWORD = page.locator("#password")
        self.CONFIRM_PASSWORD = page.locator("#password-confirm")
        self.REGISTER_BUTTON = page.get_by_role("button", name="Зарегистрироваться")

        self.USERNAME = page.locator("#username")
        self.LOGIN_BUTTON = page.get_by_role("button", name="Войти")

        self.PHONE_TAB = page.get_by_text("Телефон", exact=True)
        self.MAIL_TAB = page.get_by_text("Почта")
        self.LOGIN_TAB = page.get_by_text("Логин")
        self.SELF_ACCOUNT_TAB = page.get_by_text("Лицевой счёт")

        self.FORGOT_PASSWORD = page.get_by_role("link", name="Забыл пароль")
        self.CONTINUE_BUTTON = page.get_by_role("button", name="Продолжить")

        self.HELP_BUTTON = page.get_by_text("Помощь")
        self.HELP_HEADER = page.get_by_role("heading", name="Ваш безопасный ключ к сервисам Ростелекома")

        self.TERMS_OF_USE_BUTTON = page.get_by_role("link", name="пользовательского соглашения")

        self.INCORRECT_NUMBER = page.get_by_text("Неверный формат телефона")

        self.INCORRECT_LOGINPASSWORD = page.get_by_text("Неверный логин или пароль")

        self.LOGIN_WITH_VK_BUTTON = page.locator("#oidc_vk")
        self.LOGIN_WITH_OK_BUTTON = page.locator("#oidc_ok")
        self.LOGIN_WITH_MAIL_BUTTON = page.locator("#oidc_mail")
        self.LOGIN_WITH_YANDEX_BUTTON = page.locator("#oidc_ya")

        self.COOKIES_BUTTON = page.get_by_text("Cookies")
        self.COOKIES_USE = page.get_by_text("Мы используем Cookie")