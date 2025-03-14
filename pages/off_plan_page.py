from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class OffPlanPage(BasePage):

    OFFPLAN_TEXT = (By.CSS_SELECTOR, "[href='/'],[text='Off-plan']")
    OFFPLAN_LINK = (By.CSS_SELECTOR, "div.menu-button-text")
    OFFPLAN_ANNOUNCED = (By.CSS_SELECTOR, "[wized='projectStatus'],[w-el-text='Status'],[text='Announced']")
    OFFPLAN_PRESALE = (By.CSS_SELECTOR, "[wized='projectStatus'],[w-el-text='Status'],[text='Presale(EOI)']")


    def click_off_plan_link(self):
        elements = self.driver.find_elements(*self.OFFPLAN_LINK)
        elements[1].click()
        sleep(10)


    def verify_offplan_link_open_successfully(self):
        expected_result = 'Off-plan'
        elements = self.driver.find_elements(*self.OFFPLAN_TEXT)
        actual_result = elements[3].text
        sleep(10)
        print(expected_result, actual_result)
        assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
        self.verify_partial_text('Off-plan', *self.OFFPLAN_TEXT)

# Scenario 28
    def click_sale_status_and_select_announced(self):
       elements = self.driver.find_elements(By.CSS_SELECTOR, "[id='Location-2'],[wized='saleStatusFilter'],[value='Announced']")
       elements[1].click()
       sleep(10)


    def verify_offplan_sale_status_announced_open_successfully(self):
        expected_result = "Announced"
        elements = self.driver.find_elements(*self.OFFPLAN_ANNOUNCED) # Use find_elements to get multiple elements

        for element in elements:
            actual_result = element.text  # Ensure text is stripped of leading/trailing spaces
            print(f"Expected: {expected_result}, Actual: {actual_result}")
            assert expected_result in actual_result, f"Assertion failed: Expected '{expected_result}' in '{actual_result}'"

# Scenario 29
    def click_sale_status_and_select_presale(self):
       self.driver.find_element(By.CSS_SELECTOR, "[id='Location-2'],[wized='saleStatusFilter'].select-field-3 w-select").click()
       sleep(10)


    def verify_offplan_sale_status_presale_open_successfully(self):
        expected_result = "Presale(EOI)"
        elements = self.driver.find_elements(*self.OFFPLAN_PRESALE) # Use find_elements to get multiple elements

        for element in elements:
            actual_result = element.text  # Ensure text is stripped of leading/trailing spaces
            print(f"Expected: {expected_result}, Actual: {actual_result}")
            assert expected_result in actual_result, f"Assertion failed: Expected '{expected_result}' in '{actual_result}'"