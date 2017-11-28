from selenium.webdriver.common.by import By
from browser import Browser


class HomePageLocator(object):
    expected_elements = {'main navigation bar': '.main-navigation',
                         'options bar': '.options-bar',
                         'top bar': '.top-bar'}


class HomePage(Browser):

    def click_element(self, context, element):
        expected_elements = {'menu button': '.jump-to-menu'}
        for k,v in expected_elements.items():
            if k == element:
                element = v
            else:
                element = None

        super(HomePage, self).click_element(context, element)

    def get(self, url):
        self.driver.get(url)

    def assert_element_exists(self, context, element):
        if element not in HomePageLocator.expected_elements:
            raise Exception('The element passed in does not exist in expected elements'
                            'Actual: {}, Expected: {}'.format(element, self.expected_elements))

        for k, v in HomePageLocator.expected_elements.items():
            if element == k:
                my_elem = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.CSS_SELECTOR, element)))
                assert my_elem.is_displayed() == True, "Element does not exist! {}".format(element)
                print("locating: ", k, v)