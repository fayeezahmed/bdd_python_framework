from behave import given, when, then


@given("I am at the home page")
def at_home_page(context):

    print("I am the code that will open browser and go to home page")
    print("I am the code that will open browser and go to home page")
    print("I am the code that will open browser and go to home page")

@given("I am printing this {keyword}")
def keyword_printing(context, keyword):
    if not keyword:
        raise "Specify the keyword in Given statement!"
    print("IT WORKED!")

@when('I click on "contact us"')
def click_contact_us(context):

    print('I am clicking on the "contact us" ')
    

@then("I should see 123 Testing St.")
def verify_address(context):

    print("I see the correct address")


@when("I click on my account")
def click_my_account(context):

    print("I am clicking on my account")

@then("I should see 'Preferences'")
def see_prefernces(context):

    print("Should see preferences")
    assert 1 == 2, "one is not same as two"