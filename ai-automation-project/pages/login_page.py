import allure
from playwright.sync_api import Page

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.page_title = page.locator(".title")

    @allure.step("Open login page")
    def open(self):
        self.page.goto(self.URL)

    @allure.step("Login with username: {username}")
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("Get page title")
    def get_title(self):
        return self.page_title.inner_text()
