from behave import *

import CommonStep
import WebElements


@given('I verify that I successfully login to VS Monitor with "{expected_email}"')
def i_verify_that_i_successfully_login_to_vs_monitor(context, expected_email):
    element_email = CommonStep.presence_element_located_find_by_xpath(context, WebElements.GET_EMAIL_NAVIGATION_MENU)
    print(element_email.text)

    if element_email.text != expected_email:
        raise AssertionError(f"Did not get the expected user email: {expected_email} but get {element_email.text}")


@then('I verify that the "{error_message}" should be displayed')
def i_verify_that_the_error_message_should_be_displayed(context, error_message):
    element_error_message = CommonStep.presence_element_located_find_by_id(context, WebElements.GET_LOGIN_ERROR_MESSAGE)

    if not element_error_message.is_displayed() and element_error_message.text != error_message:
        raise AssertionError("Error message not display")


@then('I verify that I able to navigate to Dashboard at "{expected_url}"')
def i_validate_that_i_navigate_to_my_user_account(context, expected_url):
    element_dashboard_label = CommonStep.visibility_element_located_find_by_xpath(context,
                                                                                  WebElements.GET_DASHBOARD_LABEL)

    actual_url = context.driver.current_url

    if not element_dashboard_label.is_displayed() and actual_url != expected_url:
        raise AssertionError(
            f"Did not navigate to expected url: {expected_url}, but navigate to: {actual_url}")
