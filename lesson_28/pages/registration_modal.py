from selenium.webdriver.common.by import By
from lesson_28.pages.base_ops import BaseOps


class RegistrationModal(BaseOps):

    FIRST_NAME = (By.CSS_SELECTOR, "#signupName")
    LAST_NAME = (By.CSS_SELECTOR, "#signupLastName")
    EMAIL = (By.CSS_SELECTOR, "#signupEmail")
    PASSWORD = (By.CSS_SELECTOR, "#signupPassword")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#signupRepeatPassword")
    REGISTER_BTN = (By.XPATH, "//button[text()='Register']")

    def find_first_name_input_field(self):
        return self.find(self.FIRST_NAME)

    def find_last_name_input_field(self):
        return self.find(self.LAST_NAME)

    def find_email_input_field(self):
        return self.find(self.EMAIL)

    def find_password_input_field(self):
        return self.find(self.PASSWORD)

    def find_repeat_password_input_field(self):
        return self.find(self.REPEAT_PASSWORD)

    def find_register_button(self):
        return self.find(self.REGISTER_BTN)
