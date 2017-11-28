Feature: Verifying the home page url

  Scenario: The home page should have the correct title

    Given I go to the site "http://www.python.org"
    Then the title of the page should be "Welcome to Python.org"

  Scenario: The home page should have the correct url

    Given I go to the site "http://www.python.org"
    Then the url should be "https://www.python.org"