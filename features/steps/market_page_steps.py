from behave import given, when, then

@then('Open the market page')
def open_market_companies(context):
    context.app.market_page.open_market_companies()

@then('User click on market link at the left side in menu')
def click_market_link(context):
   context.app.market_page.click_market_link()

@then('Verify market page opened')
def verify_market_link_open_successfully(context):
    context.app.market_page.verify_market_link_open_successfully()