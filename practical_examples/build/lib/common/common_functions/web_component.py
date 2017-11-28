from selenium import webdriver

def go_to(url, browser="Firefox"):
    """
    :param url: url of the page you are visiting
    :param browser: browser you are using, default is Firefox
    :return: driver: returns the webdriver
    """

    # create an instance of the firefox driver
    if browser == "Firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Please specify the Firefox driver")

    # clean up url and go to url
    url = url.strip()
    driver.get(url)

    return driver

def assert_text(actual, expected):
    """
    Function to assert general text strings
    :param actual:
    :param expected:
    :return:
    """

    assert expected == actual, "The text does not match:\n\tactual : {0} \n\texpected : {1}\n"

def assert_page_title(context, expected_title):
    """
    Function to assert the page title
    :param context:
    :param expected_title:
    :return:
    """

    actual_title = context.driver.title

    assert expected_title == actual_title, "The title does not match"

def assert_url(context, expected_url):
    """
    Function to assert the url
    :param context:
    :param expected_url:
    :return:
    """
    print(dir(context.driver))
    actual_url = context.driver.current_url.rstrip('/')
    print("\t ACTUAL URL: {}".format(actual_url))
    assert expected_url == actual_url

def assert_element_exists(element):
    pass