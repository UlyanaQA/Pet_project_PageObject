from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        # link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        # link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()


    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"