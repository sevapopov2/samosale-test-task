Feature: Login Page

  Background:
    Given login page is opened

  Scenario: User checks a phone field
    When user finds a phone field
    Then user enters phone number
    Then user presses sign in button
    Then error message displays

Scenario: User checks an empty phone field
    When user finds a phone field
    Then user presses sign in button
    Then error message displays
