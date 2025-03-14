from behave import given, when, then

@then('User click on Secondary link at the left side in menu')
def open_secondary(context):
   context.app.secondary_page.open_secondary()

@then('Verify Secondary page opened')
def verify_secondary_link_open_successfully(context):
    context.app.secondary_page.verify_secondary_link_open_successfully()