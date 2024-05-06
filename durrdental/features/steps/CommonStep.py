import time

import WebElements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver

TIMEOUT = 10


@given('I am on "{url}" - VS Monitor Homepage')
def i_am_on_vs_monitor_homepage(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given('I enter "{username}" for username and "{password}" for password')
def i_enter_the_credential(context, username, password):
    element_username = get_username_element(context)
    element_username.send_keys(username)

    element_password = get_password_element(context)
    element_password.send_keys(password)


@when('I click on Login button in VS Monitor Homepage')
def i_click_on_login_button_in_vs_monitor_homepage(context):
    element = WebDriverWait(context.driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.XPATH, WebElements.GET_LOGIN_BUTTON_AT_HOMEPAGE)))
    element.click()


@when('I click on LOG-IN button on Log-in page')
def i_click_on_login_button_on_login_page(context):
    element_login_button = get_login_button_in_login_page(context)
    element_login_button.submit()


@then("I validate that I navigate to Login page")
def i_able_to_validate_that_i_navigate_to_login_page(context):
    element_login_label = get_login_label_element(context)
    element_username = get_username_element(context)
    element_password = get_password_element(context)
    element_login_button = get_login_button_element(context)

    if (not element_login_label and not element_username.is_displayed()
            and not element_password.is_displayed() and not element_login_button.is_displayed()):
        get_element_in_login_page_is_displayed(element_login_label, element_password, element_username,
                                               element_login_button)
        raise AssertionError("Element not found")


def get_login_label_element(context):
    return WebDriverWait(context.driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, WebElements.GET_LOGIN_LABEL_AT_LOGIN_PAGE)))


def get_username_element(context):
    return WebDriverWait(context.driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, WebElements.GET_USERNAME_INPUT_AT_LOGIN_PAGE)))


def get_password_element(context):
    return WebDriverWait(context.driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, WebElements.GET_PASSWORD_INPUT_AT_LOGIN_PAGE)))


def get_login_button_element(context):
    return WebDriverWait(context.driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, WebElements.GET_LOGIN_BUTTON_AT_LOGIN_PAGE)))


def get_element_in_login_page_is_displayed(element_login_label, element_password, element_username,
                                           element_login_button):
    print("element_login_label : ", element_login_label.is_displayed())
    print("element_username : ", element_username.is_displayed())
    print("element_password : ", element_password.is_displayed())
    print("element_login_button : ", element_login_button.is_displayed())


def get_login_button_in_login_page(context):
    return WebDriverWait(context.driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, WebElements.GET_LOGIN_BUTTON_AT_LOGIN_PAGE)))
