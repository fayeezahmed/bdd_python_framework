from behave import given, when, then
from python_org.pages.home_page import HomePage


@given('I go to the site "{url}"')
def go_to_url(context, url):
    """
    :param context:
    :param url:
    :return:
    """
    print("Navigating to the site {}:".format(url))
    context.homepage.get(url)


@then('the title of the page should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies page title is as expected
    :param context:
    :param expected_title:
    :return:
    """
    context.homepage.assert_text(context.browser.driver.title, expected_title)


@then('the url should be "{expected_url}"')
def verify_url(context, expected_url):
    """
    Verifiies the url is as expected
    :param context:
    :param expected_url:
    :return:
    """
    context.homepage.assert_text(context.browser.driver.current_url, expected_url)

@when('I click on the "{element}"')
def click_element(context, element):
    """
    Click on elements within the page
    :param context:
    :param element:
    :return:
    """

    context.homepage.click_element(context, element)

@then('the "{element}" should be visible')
def verify_element_is_visible(context, element):
    """
    Verifies that the element exists
    :param element:
    :return:
    """
