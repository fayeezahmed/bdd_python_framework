from behave import given, when, then
from common.common_functions import web_component

@given('I go to the site "{url}"')
def go_to_url(context, url):
    """
    :param context:
    :param url:
    :return:
    """
    print("Navigating to the site {}:".format(url))

    # save the web driver in a context variable to pass it around
    context.driver = web_component.go_to(url)

@then('the title of the page should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies page title is as expected
    :param context:
    :param expected_title:
    :return:
    """
    web_component.assert_text(context.driver.title, expected_title)

@then('the url should be "{expected_url}"')
def verify_url(context, expected_url):
    """
    Verifiies the url is as expected
    :param context:
    :param expected_url:
    :return:
    """
    web_component.assert_text(context.driver.current_url, expected_url)
