from selenium.webdriver.common.by import By
from symtable import Class
from time import sleep
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    LOGIN = (By.XPATH, "//a[@wized='loginButton']")
    VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")


    def enter_email(self, email):
        self.input_text(email, *self.EMAIL)


    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD)
        sleep(2)


    def click_continue_button(self):
        self.click(*self.LOGIN)
        sleep(2)


