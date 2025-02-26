from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class SignupPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SIGNUP_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    ERROR_MESSAGE = (By.CLASS_NAME, "message-error")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Actions
    def enter_signup_details(self, first_name, last_name, email, password):
        self.find_element(self.FIRST_NAME).send_keys(first_name)
        self.find_element(self.LAST_NAME).send_keys(last_name)
        self.find_element(self.EMAIL).send_keys(email)
        self.find_element(self.PASSWORD).send_keys(password)
        self.find_element(self.CONFIRM_PASSWORD).send_keys(password)

    def click_signup_button(self):
        self.find_element(self.SIGNUP_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
