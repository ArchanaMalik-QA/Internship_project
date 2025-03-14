from behave import given, when, then

@then('User click on off-plan link at the left side in menu')
def click_off_plan_link(context):
    context.app.off_plan_page.click_off_plan_link()

@then('Verify off_plan page opened')
def verify_offplan_link_open_successfully(context):
    context.app.off_plan_page.verify_offplan_link_open_successfully()

@then('Filter by sale status as Announced')
def click_sale_status_and_select_announced(context):
    context.app.off_plan_page.click_sale_status_and_select_announced()

@then('Verify each product contains the Announced')
def verify_offplan_sale_status_announced_open_successfully(context):
   context.app.off_plan_page.verify_offplan_sale_status_announced_open_successfully()

# Scenario 29:  User can filter by Presale
@then('Filter by sale status as Presale')
def click_sale_status_and_select_presale(context):
    context.app.off_plan_page.click_sale_status_and_select_presale()

@then('Verify each product contains the Presale')
def verify_offplan_sale_status_presale_open_successfully(context):
   context.app.off_plan_page.verify_offplan_sale_status_presale_open_successfully()