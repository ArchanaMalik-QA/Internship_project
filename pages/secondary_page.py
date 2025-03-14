from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class SecondaryPage(BasePage):

    SECONDARY_TEXT = (By.CSS_SELECTOR, ".menu-text-link-leaderboard.w--current")
    SECONDARY_LINK = (By.CSS_SELECTOR, "[href='/secondary-listings']")

    def open_secondary(self):
        self.driver.find_element(*self.SECONDARY_LINK).click()
        sleep(10)


    def verify_secondary_link_open_successfully(self):
        expected_result = 'Secondary'
        actual_result = self.driver.find_element(*self.SECONDARY_TEXT).text
        print(expected_result, actual_result)
        assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
        self.verify_partial_text('Secondary', *self.SECONDARY_TEXT)

sleep(2)