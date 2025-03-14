from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

from support.logger import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Google Chrome Setting
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


#firefox setting
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager
# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
### Google Chrome
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Enable capturing of the browser logs:
    #chrome_options = Options()

    # chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service, options=chrome_options)


# -------------------
### Firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # firefox_options = Options()
    # context.driver = webdriver.Firefox(service=service, options=firefox_options)

# -------------------
### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
#-------------------
# ### BROWSERSTACK ###
#     ##Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
#     bs_user = 'archanamalik_8egyvF'
#     bs_key = 'bXJdyy3gnxWpmqAkAsez'
#     url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#
#     options = Options()
#     bstack_options = {
#         "os": "Windows",
#         "osVersion": "11",
#         'browserName': 'Chrome',
#         'sessionName': scenario_name,
#     }
#     options.set_capability('bstack:options', bstack_options)
#     context.driver = webdriver.Remote(command_executor=url, options=options)
#------------------

    # # Mobile emulation settings (example for an iPhone)
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 430, "height": 932, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    #     "clientHints": {"platform": "Android", "mobile": True}}
    #
    # # Set up Chrome options
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Initialize WebDriver with the mobile emulation settings
    # context.driver = webdriver.Chrome(options=chrome_options)

#----------------------------------------------

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    # Add browser logs:
    # browser_logs = context.driver.get_log('browser')
    # with open("browser_logs.txt", "w") as log_file:
    #     for log_entry in browser_logs:
    #         log_file.write(f"{log_entry['level']} - {log_entry['timestamp']} - {log_entry['message']}\n")
    # print("Browser logs have been saved to browser_logs.txt")

    context.driver.quit()