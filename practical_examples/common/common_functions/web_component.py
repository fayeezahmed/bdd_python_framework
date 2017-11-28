from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def go_to(context, url):
    """
    :param url: url of the page you are visiting
    :param browser: browser you are using, default is Firefox
    :return: driver: returns the webdriver
    """

    # clean up url and go to url
    url = url.strip()
    context.browser.get(url)


def assert_text(actual, expected):
    """
    Function to assert general text strings
    :param actual:
    :param expected:
    :return:
    """
    actual_stripped = actual.rstrip('/')
    assert expected == actual_stripped, "The text does not match:\n\tExpected : {0} \n\tActual : {1}\n".format(expected, actual_stripped)


def assert_element_exists(context, element):
    my_elem = WebDriverWait(context.browser, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, element)))
    assert my_elem.is_displayed() == True, "Element does not exist! {}".format(element)


def click_element(context, element):
    my_elem = WebDriverWait(context.browser, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, element)))
    my_elem.click()
