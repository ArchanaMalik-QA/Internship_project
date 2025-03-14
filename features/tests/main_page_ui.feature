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


  # Scenario 28 : User can filter by Announced
    Scenario: User can open off-plan tab and check for sale status as announced
    Given Open the main page
    When Enter the email
    Then Enter the password
    Then Click continue button
    Then User click on off-plan link at the left side in menu
    Then Verify off_plan page opened
    Then Filter by sale status as Announced
    Then Verify each product contains the Announced

  # Scenario 29 : User can filter by Presale
    Scenario: User can filter by Presale
    Given Open the main page
    When Enter the email
    Then Enter the password
    Then Click continue button
    Then User click on off-plan link at the left side in menu
    Then Verify off_plan page opened
    Then Filter by sale status as Presale
    Then Verify each product contains the Presale

  # Scenario 30 : User can filter by Out of stock
    Scenario: User can filter by Out of stock
    Given Open the main page
    When Enter the email
    Then Enter the password
    Then Click continue button
    Then User click on off-plan link at the left side in menu
    Then Verify off_plan page opened
    Then Filter by sale status as Out of stock
    Then Verify each product contains the Out of stock


