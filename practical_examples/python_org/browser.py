from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Browser(object):

    driver = webdriver.Firefox()
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def assert_text(self,actual, expected):
        """
        Function to assert general text strings
        :param actual:
        :param expected:
        :return:
        """
        actual_stripped = actual.rstrip('/')
        assert expected == actual_stripped, "The text does not match:\n\tExpected : {0} \n\tActual : {1}\n".format(expected, actual_stripped)

    def assert_element_exists(self, context, element):
        my_elem = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, element)))
        assert my_elem.is_displayed() == True, "Element does not exist! {}".format(element)

    def click_element(self, context, element):
        my_elem = WebDriverWait(context.browser, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, element)))
        return my_elem.click()
