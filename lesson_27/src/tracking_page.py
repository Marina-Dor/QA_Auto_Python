from datetime import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrackingPage:
    def __init__(self, driver):
        # Initializing the TrackingPage class with a Selenium WebDriver instance
        # and defining element locators as tuples for further use with element search methods
        self.driver = driver
        # Locator for the tracking input field
        self.tracking_input = (By.CSS_SELECTOR, "input[class='track__form-group-input']")
        # Locator for the search button
        self.search_button = (By.CSS_SELECTOR, "np-number-input-desktop-btn-search-en")
        # Locator for the search status text element
        self.search_received_status_text = (By.CSS_SELECTOR, "div.header__status-text")
        self.error_status_text = (By.CSS_SELECTOR, "div.track__form-message.track__form-error span")

    def open(self):
        # Opens the Nova Poshta tracking page.
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def enter_tracking_number(self, tracking_number, submit_with_button=False):
        # Entering the tracking number into the input field and submitting the form
        # Variable submit_with_button: If True, the form is submitted by clicking the submit button.
        # Otherwise, the Enter key is used

        # Waiting for the input field to be displayed
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.tracking_input)
        )
        input_element.clear()  # Clear the field (delete placeholder text)
        input_element.send_keys(tracking_number)

        if submit_with_button:
            # Waiting for the button to be clickable (enabled and green)
            button_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_button)
            )
            button_element.click()
        else:
            # Press the Enter key to submit the form
            input_element.send_keys(Keys.RETURN)

    def get_received_status(self):
        # Retrieving the current status text from the tracking page.

        # Waiting for the status text to be visible
        status_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_received_status_text)
        )
        return status_text_element.text

    def get_error_status(self):
        status_text_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_status_text)
        )
        return status_text_element.text
