from selenium.webdriver.common.by import By


class CodePageLocators:
    CHECKBOX_ROBOT = (By.CSS_SELECTOR, 'form input[name="robot"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'form > button[type=submit]')
    SECRET_INPUT = (By.CSS_SELECTOR, 'form > input[name=secret]')
    CODE_INPUT = (By.CSS_SELECTOR, 'input[name="code"]')
