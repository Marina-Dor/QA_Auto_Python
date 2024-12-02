from selenium.webdriver.common.by import By
from lesson_28.pages.base_ops import BaseOps


class MyProfile(BaseOps):
    MY_PROFILE = (By.CSS_SELECTOR, "#userNavDropdown")

    def find_my_profile_menu(self):
        return self.wait_for(self.MY_PROFILE)
