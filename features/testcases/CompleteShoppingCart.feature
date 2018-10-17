# Please note this is NOT the best way to write Cucumber as it should not be technical and should focus on business value
  # However, this is only being used to demonstrate Automation practice excercises
Feature: Login to portal

  # Scenario: Login and logout
  #   When I open automationpractice website "http://www.automationpractice.com"
  #   And I login with username "automationqa@test.com" and password "Pass1234"
  #   Then I verify that I successfully logged in by logging out

  Scenario: Confirm order and verify success message
    When I open automationpractice website "http://www.automationpractice.com"
    And I login with username "automationqa@test.com" and password "Pass1234"
    And I hover on women menu item and click summer dresses
    And I add a summer dress to cart
    And I verify the item and price
    And I verify the address and proceed
    And I verify shipping address and proceed
    And I select payment method
    And I confirm the order
    Then I verify successful purchase
