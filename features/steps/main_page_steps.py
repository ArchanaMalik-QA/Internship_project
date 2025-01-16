from behave import given, when, then


@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()




