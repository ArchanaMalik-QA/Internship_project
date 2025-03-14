from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.market_page import MarketPage
from pages.off_plan_page import OffPlanPage
from pages.pagination_number import PaginationNumber
from pages.secondary_page import SecondaryPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.market_page = MarketPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.pagination_number = PaginationNumber(driver)
        self.secondary_page = SecondaryPage(driver)