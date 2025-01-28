from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class MarketPage(BasePage):

    MARKET_TEXT = (By.CSS_SELECTOR, "div.page-title.agency")
    MARKET_LINK = (By.CSS_SELECTOR, "[href='/market-companies']")

    def open_market_companies(self):
        self.open_url('https://soft.reelly.io/market-companies')
        sleep(10)

    def click_market_link(self):
        self.driver.find_element(By.CSS_SELECTOR, "[href='/market-companies']").click()
        print("market link clicked")


    def verify_market_link_open_successfully(self):
        expected_result = 'Market'
        actual_result = self.driver.find_element(*self.MARKET_TEXT).text
        print(expected_result, actual_result)
        assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
        self.verify_partial_text('Market', *self.MARKET_TEXT)

sleep(2)