import pytest


def test_user_registration(driver, open_main_page, start_registration, fill_and_submit_registration_form,
                           redirection_to_my_profile):
    open_main_page()
    start_registration()
    fill_and_submit_registration_form()

    # Asserting registration was successful - redirect to My Profile page takes place
    assert redirection_to_my_profile(), "User is not on the profile page after registration."
