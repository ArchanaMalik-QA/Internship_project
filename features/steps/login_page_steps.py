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



