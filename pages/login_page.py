from selenium.webdriver.common.by import By
from symtable import Class
from time import sleep
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    LOGIN = (By.XPATH, "//a[@wized='loginButton']")
    VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")
    MARKET_TEXT = (By.CSS_SELECTOR, "div.page-title.agency")
    MARKET_LINK = (By.CSS_SELECTOR, "[href='/market-companies']")

    def enter_email(self, email):
        self.input_text(email, *self.EMAIL)


    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD)
        sleep(2)


    def click_continue_button(self):
        self.click(*self.LOGIN)
        sleep(2)


    def click_market_link(context):
        context.driver.find_element(By.CSS_SELECTOR, "[href='/market-companies']").click()
        print("market link clicked")


    def verify_market_link_open_successfully(self):
        expected_result = 'Market'
        actual_result = self.driver.find_element(*self.MARKET_TEXT).text
        print(expected_result, actual_result)
        assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
        self.verify_partial_text('Market', *self.MARKET_TEXT)
    sleep(2)