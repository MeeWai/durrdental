# xpath
GET_LOGIN_BUTTON_AT_HOMEPAGE = '//span[contains(text(),\'Login\')]'

GET_LOGIN_LABEL_AT_LOGIN_PAGE = '//h1[contains(text(),\'Log-in\')]'

GET_LOGIN_BUTTON_AT_LOGIN_PAGE = '//button[contains(text(),\'Log-in\')]'

GET_DASHBOARD_LABEL = '//h2[contains(text(),\'Dashboard\')]'

GET_USER_NAVIGATION_MENU_BUTTON = '//div[contains(@aria-label, \'nav-user-button\')]'

GET_OPEN_SIDEBAR = '//button[contains(@aria-label,\'open-sidebar-btn\')]'

GET_USER_NAVIGATION_MENU_DESKTOP = '//div[contains(@id,\'nav-desktop\')]' + GET_USER_NAVIGATION_MENU_BUTTON

GET_USER_NAVIGATION_MENU_MOBILE = '//div[contains(@id,\'nav-mobile\')]' + GET_USER_NAVIGATION_MENU_BUTTON

GET_MY_USER_ACCOUNT_LABEL = '//span[contains(text(),\'My user account\')]'

# id
GET_USERNAME_INPUT_AT_LOGIN_PAGE = 'username'

GET_PASSWORD_INPUT_AT_LOGIN_PAGE = 'password'

GET_LOGIN_ERROR_MESSAGE = 'error-password'

GET_USER_PROFILE = 'user-profile'

GET_USER_FIRST_NAME = 'firstName'

GET_USER_LAST_NAME = 'lastName'

GET_USER_EMAIL = 'email'
