import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage

@allure.title("Login Test - AI Assisted (Cursor + Ollama)")
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", "Products"),
    ("locked_out_user", "secret_sauce", None)
])
def test_login_ai(page: Page, username: str, password: str, expected: str):
    """
    AI Global (Cursor / Copilot):
    - Suggested POM structure & parametrization
    AI Local (Ollama):
    - Added negative test case & improved assertion
    Human touch:
    - Final polish + Allure integration
    """
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    if expected:
        assert login_page.get_title() == expected, \            f"[AI Local] Expected {expected}, got {login_page.get_title()}"
    else:
        with allure.step("Verify locked out message (Ollama refinement)"):
            assert page.locator("h3").inner_text().startswith("Epic sadface")
