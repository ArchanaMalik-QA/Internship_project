# Created by archanamalik at 12/9/24
Feature: Tests for Main page UI

  Scenario: User can open market tab and go through the pagination
    Given Open the main page
    When Enter the email
    Then Enter the password
    Then Click continue button
    Then User click on market link at the left side in menu
    Then Verify market page opened
    Then Go to the final page using the pagination button
    Then Go back to the first page using the pagination button


