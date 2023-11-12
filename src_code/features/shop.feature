Feature: Shop

  Scenario Outline: Shop an item
    Given I go to the storefront
    When I click on add <quantity> times for <item_name>
      And I proceed to checkout
    Then I verify <item_name> was added to the cart <quantity> times
      And I verify subtotal equals <item_expected_price> by <quantity>
      And I verify taxes amount $1.50 by <quantity>

    Examples:
    |item_name    |item_expected_price  |quantity|
    |Experimental |25                   |2       |

  @Browser:firefox
  Scenario: All cards are displayed
    Given I go to the storefront
    Then I verify all items are displayed