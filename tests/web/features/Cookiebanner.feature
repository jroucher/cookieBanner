Feature: Cookie banner

  @TC-id(1)
  Scenario: Check cookie banner in the homepage
    Given goto page
	Then cookie banner present

  @TC-id(2)
  Scenario: Cookie banner disappear when accept
    Given goto page
	Then click on accept
	And cookie banner disappears