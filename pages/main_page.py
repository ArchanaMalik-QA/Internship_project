from pages.base_page import BasePage
from time import sleep

class MainPage(BasePage):

    def open_main(self):
        self.open_url('https://soft.reelly.io')
        sleep(10)
