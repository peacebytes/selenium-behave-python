Feature: Login to portal

  Scenario: Login and logout
    When I open automationpractice website "http://www.automationpractice.com"
    And I login with username "automationqa@test.com" and password "Pass1234"
    Then I verify that I successfully logged in by logging out
