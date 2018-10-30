Feature: Login to portal

  Scenario: Login and logout
    When I open automationpractice website
    And I login automationpractice website
    Then I verify that I successfully logged in by logging out
