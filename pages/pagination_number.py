from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage


class PaginationNumber(BasePage):

    #market page elements
    #TOTAL_PAGES_NUMBER = (By.CSS_SELECTOR, "[wized='totalPageMarket']")

    # secondary page elements
    TOTAL_PAGES_NUMBER = (By.CSS_SELECTOR, "[wized='totalPageProperties']")

    #market page elements
    #NEXT_PAGE_ARROW_BUTTON = (By.CSS_SELECTOR,"[wized='nextPageMarket']")

    # secondary page elements
    NEXT_PAGE_ARROW_BUTTON = (By.CSS_SELECTOR,"[wized='nextPageMLS']")

    #market page elements
    #PREVIOUS_PAGE_ARROW_BUTTON = (By.CSS_SELECTOR, "[wized='previousPageMarket']")

    # secondary page elements
    PREVIOUS_PAGE_ARROW_BUTTON = (By.CSS_SELECTOR, "[wized='previousPageMLS']")

    #market page elements
    #CURRENT_PAGE = (By.CSS_SELECTOR, "[wized='currentPageMarket']")

    #secondary page elements
    CURRENT_PAGE = (By.CSS_SELECTOR, "[wized='currentPageProperties']")

    def go_to_finalpage_pagination(self, *locator):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #self.driver.find_element(*self.TOTAL_PAGES_NUMBER).click()
        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES_NUMBER).text)
        current_page = int(self.driver.find_element(*self.CURRENT_PAGE).text)
        print(f"Current pages: {current_page}")
        print(f"Total pages: {total_pages}")


        # Navigate through all pages using a for loop
        for page in range(current_page, total_pages + 1 ):
            # Locate and interact with the page input or buttons (update selector as needed)
            wait = WebDriverWait(self.driver, 15)
            sleep(6)
            print(f"Successfully loaded page {page}.")
            if page != total_pages:
                #self.driver.execute_script("window.scrollBy(0,2000)", "")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next_page_arrow_button = wait.until(EC.visibility_of_element_located(self.NEXT_PAGE_ARROW_BUTTON))
                next_page_arrow_button.click()
        print("Successfully reached the last page.")
        current_page_after_loop = int(self.driver.find_element(*self.CURRENT_PAGE).text)
        print(f"Current pages after loop: {current_page_after_loop}")
        assert current_page_after_loop == total_pages , 'Did not reach last page'
        print("Pagination testing completed successfully!")


    def go_backto_firstpage_pagination(self, *locator):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.TOTAL_PAGES_NUMBER).click()
        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES_NUMBER).text)
        current_page = int(self.driver.find_element(*self.CURRENT_PAGE).text)
        print(f"Current pages: {current_page}")
        print(f"Total pages: {total_pages}")

        # Navigate through all pages using a for loop
        for page in range(total_pages,0,-1):
            # Locate and interact with the page input or buttons (update selector as needed)
            wait = WebDriverWait(self.driver, 15)
            sleep(6)

            previous_page_arrow_button = wait.until(EC.visibility_of_element_located(self.PREVIOUS_PAGE_ARROW_BUTTON))
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print(f"Successfully loaded page {page}.")
            if page != 1:
                previous_page_arrow_button.click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Successfully reached the last page.")
        current_page_after_loop = int(self.driver.find_element(*self.CURRENT_PAGE).text)
        print(f"Current pages after loop: {current_page_after_loop}")
        assert current_page_after_loop == 1, 'Did not reach first page'
        print("Down Pagination testing completed successfully!")