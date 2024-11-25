import pytest
from selenium import webdriver
from lesson_27.src.tracking_page import TrackingPage


@pytest.fixture
def driver():
    # Setting up and tearing down the Selenium WebDriver for Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


"""
Verifying that the tracking form can be submitted using Submit button 
Comparing the text of the status received
"""


@pytest.mark.parametrize(
    "tracking_number, expected_status, submit_with_button",
    # Submit with Button click
    [("20451020580305", "Отримана", True)]
)
def test_tracking_received_status_submit_button(driver, tracking_number, expected_status, submit_with_button):
    # Creating TrackingPage object
    tracking_page = TrackingPage(driver)
    tracking_page.open()

    # Entering correct tracking number
    tracking_page.enter_tracking_number(tracking_number)
    # Retrieving actual status text
    actual_status = tracking_page.get_received_status()

    # Comparing actual status with expected
    assert actual_status == expected_status, "The status does not match the expected value"


"""
Verifying that the tracking form can be submitted using Enter key 
Comparing the text of the status received
"""


@pytest.mark.parametrize(
    "tracking_number, expected_status, submit_with_button",
    # Submit with Enter key
    [("20451020580305", "Отримана", False)]
)
def test_tracking_received_status_submit_enter(driver, tracking_number, expected_status, submit_with_button):
    # Creating TrackingPage object
    tracking_page = TrackingPage(driver)
    tracking_page.open()

    # Entering correct tracking number
    tracking_page.enter_tracking_number(tracking_number)
    # Retrieving actual status text
    actual_status = tracking_page.get_received_status()
    # Comparing actual status with expected
    assert actual_status == expected_status, "The status does not match the expected value"


"""
Verifying that the tracking form can be submitted using Enter key 
Comparing the text of the error status 
"""


@pytest.mark.parametrize(
    "tracking_number, expected_status, submit_with_button",
    [("12345678910", "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, "
                     "якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609", False)]
)
def test_tracking_error_status(driver, tracking_number, expected_status, submit_with_button):
    # Creating TrackingPage object
    tracking_page = TrackingPage(driver)
    tracking_page.open()

    # Entering incorrect but valid tracking number
    tracking_page.enter_tracking_number(tracking_number)
    # Retrieving actual status text
    actual_status = tracking_page.get_error_status()
    # Comparing actual status with expected
    assert actual_status == expected_status, "The status does not match the expected value"
