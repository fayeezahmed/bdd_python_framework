from behave import then

@then("In the subdirectory I do some stuff")
def and_again(context):
    pass

@then("I am in a Python file in the subdirectory")
def in_another_py(context):
    pass