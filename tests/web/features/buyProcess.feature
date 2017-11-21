Feature: Buy process 

  @TC-id(2) #TC – [OK] complete the checkout
  Scenario: complete the checkout
    Given goto page
    And add item to shopping cart
	Then go to shopping cart
	And at least one item is present
	Then Proceed to checkout
	And Complete the form and go next
	And Select payment method and complete payment