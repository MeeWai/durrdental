import time

from behave import *

import WebElements
import CommonStep


@then('I click on My user account on the user menu in dashboard')
def i_click_on_my_user_account_on_user_menu(context):
    element_user_navigation_menu = CommonStep.visibility_element_located_find_by_xpath(context,
                                                                                       WebElements.GET_USER_NAVIGATION_MENU)
    element_user_navigation_menu.click()

    element_user_account = CommonStep.visibility_element_located_find_by_id(context, WebElements.GET_USER_PROFILE)
    element_user_account.click()

    time.sleep(3)


@then('I verify that I able to navigate to My user account at "{expected_url}"')
def i_validate_that_i_navigate_to_my_user_account(context, expected_url):
    element_my_user_account_label = CommonStep.visibility_element_located_find_by_xpath(context,
                                                                                        WebElements.GET_MY_USER_ACCOUNT_LABEL)

    actual_url = context.driver.current_url

    if actual_url != expected_url:
        raise AssertionError(f"Did not navigate to expected url: {expected_url}, but navigate to: {actual_url}")

    if element_my_user_account_label.text != 'My user account':
        raise AssertionError(f"Wrong page displayed: {element_my_user_account_label.text}, "
                             f"expected page: My user account")


@then('I verify that "{expected_first_name}" in first name, "{expected_last_name}" in last name and "{'
      'expected_email}" in email address are correct in my user account')
def i_verify_name_email_are_correct_in_my_user_account(context, expected_first_name, expected_last_name,
                                                       expected_email):
    element_first_name = CommonStep.visibility_element_located_find_by_id(context, WebElements.GET_USER_FIRST_NAME)

    element_last_name = CommonStep.visibility_element_located_find_by_id(context, WebElements.GET_USER_LAST_NAME)

    element_email = CommonStep.visibility_element_located_find_by_id(context, WebElements.GET_USER_EMAIL)

    if element_first_name.get_attribute('value') != expected_first_name:
        raise AssertionError(
            f'Actual first name : {element_first_name.get_attribute('value')} '
            f'not equal to expected first name : {expected_first_name}')
    elif element_last_name.get_attribute('value') != expected_last_name:
        raise AssertionError(
            f'Actual last name : {element_last_name.get_attribute('value')} '
            f'not equal to expected first name : {expected_last_name}')
    elif element_email.get_attribute('value') != expected_email:
        raise AssertionError(
            f'Actual email : {element_email.get_attribute('value')} '
            f'not equal to expected email : {expected_email.text}')
