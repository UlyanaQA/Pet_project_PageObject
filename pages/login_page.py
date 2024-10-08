from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        assert "login" in self.browser.current_url, f"'{'login'}' is not found in '{self.browser.current_url}'"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"
