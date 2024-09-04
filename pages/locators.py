from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    LOG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")