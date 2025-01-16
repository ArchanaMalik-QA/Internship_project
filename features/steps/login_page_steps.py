from behave import given, when, then
from time import sleep


@when('Enter the email')
def enter_email(context):
    context.app.login_page.enter_email('archana.malik.1985@gmail.com')

@then('Enter the password')
def enter_password(context):
    context.app.login_page.enter_password('Password@123')

@then('Click continue button')
def click_continue_button(context):
    context.app.login_page.click_continue_button()
    sleep(10)

@then('User click on market link at the left side in menu')
def click_market_link(context):
   context.app.login_page.click_market_link()

@then('Verify market page opened')
def verify_market_link_open_successfully(context):
    context.app.login_page.verify_market_link_open_successfully()

