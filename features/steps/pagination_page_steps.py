from behave import  then


@then('Go to the final page using the pagination button')
def go_to_finalpage_pagination(context):
    context.app.pagination_number.go_to_finalpage_pagination(context)

@then('Go back to the first page using the pagination button')
def go_backto_firstpage_pagination(context):
    context.app.pagination_number.go_backto_firstpage_pagination(context)
