Feature: Sign up page testing

  Background:
    Given sign up page is opened

  Scenario: user checks that page is opened
    Then user finds choose messenger heading

  Scenario: user presses login link
    When user presses login link
    Then user finds sign in heading
