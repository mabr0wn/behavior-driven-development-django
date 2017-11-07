#file: features/departments.feature
Feature: Step Setup Tabl (departments)

   Scenario: Setup Table
     Given a set of specific users:
        | name      | department  |
        | Lisa      | VP Housing  |
        | John      | Call Center |
        | Mike      | Call Center |
        | Brian     | Sales       |
     When we count the number of people in each
     department
     Then we will find two people in "Call Center"
      but we will find one person in "Sales"
