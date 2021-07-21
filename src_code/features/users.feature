Feature: Users

  @Browser:firefox
  Scenario: Create a new user
    Given I go to the storefront
    When I go to the user creation screen
      And I sign up a new user
    Then I verify the new user account was created