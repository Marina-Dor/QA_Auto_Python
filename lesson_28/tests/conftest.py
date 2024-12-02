import pytest
from selenium import webdriver
from lesson_28.pages.main_page import MainPage
from lesson_28.pages.my_profile_page import MyProfile
from lesson_28.tests.tests_data import registration_query
from lesson_28.pages.registration_modal import RegistrationModal


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    def _open_main_page():
        url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
        driver.get(url)
    return _open_main_page


@pytest.fixture
def start_registration(driver):
    def _start_registration():
        main_page = MainPage(driver)
        main_page.find_sign_up_btn().click()
    return _start_registration


@pytest.fixture
def fill_and_submit_registration_form(driver):
    def _fill_and_submit_registration_form():
        registration_modal = RegistrationModal(driver)

        registration_modal.find_first_name_input_field().send_keys(registration_query["first_name"])
        registration_modal.find_last_name_input_field().send_keys(registration_query["last_name"])
        registration_modal.find_email_input_field().send_keys(registration_query["email"])
        registration_modal.find_password_input_field().send_keys(registration_query["password"])
        registration_modal.find_repeat_password_input_field().send_keys(registration_query["repeat_password"])
        registration_modal.find_register_button().click()

    return _fill_and_submit_registration_form


@pytest.fixture
def redirection_to_my_profile(driver):
    def _redirection_to_my_profile():
        my_profile = MyProfile(driver)
        try:
            my_profile.wait_for(my_profile.MY_PROFILE)  # Waiting for the element to be displayed
            return True  # Element found, return True
        except Exception as e:
            print(f"Redirection failed: {e}")
            return False  # Element not found, return False

    return _redirection_to_my_profile
