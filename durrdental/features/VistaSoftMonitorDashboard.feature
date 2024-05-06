Feature: Dashboard feature for VistaSoft Monitor IoT Solution

  Background: Login to VS Monitor System
    Given I am on "https://vsmonitor.com" - VS Monitor Homepage
    When I click on Login button in VS Monitor Homepage
    Then I validate that I navigate to Login page

  @VerifyTheUserDetailInMyUserAccount
  Scenario: Verify the user detail in My user account
    Given I enter "nmw_ng@hotmail.com" for username and "meewai123" for password
    When I click on LOG-IN button on Log-in page
    Then I click on My user account on the user menu in dashboard
    And I verify that I able to navigate to My user account at "https://vsmonitor.com/user/profile"
    And I verify that "Mee Wai" in first name, "Ng" in last name and "nmw_ng@hotmail.com" in email address are correct in my user account

