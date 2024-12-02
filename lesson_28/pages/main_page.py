from selenium.webdriver.common.by import By
from lesson_28.pages.base_ops import BaseOps


class MainPage(BaseOps):
    SIGN_UP_BUTTON = (By.XPATH, "//button[text()='Sign up']")

    def find_sign_up_btn(self):
        return self.find(self.SIGN_UP_BUTTON)
