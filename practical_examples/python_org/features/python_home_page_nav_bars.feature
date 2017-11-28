Feature: Verifying the navigation bars on the home page

  Scenario: Verify the navigation bars on the home page are visible

    Given I go to the site "http://www.python.org"
    Then the "main navigation bar" should be visible
    And the "options bar" should be visible
    And the "top bar" should be visible
