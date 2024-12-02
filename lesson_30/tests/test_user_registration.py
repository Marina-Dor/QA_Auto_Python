import allure


@allure.feature("User Registration")  # Grouping Tests by feature
def test_user_registration(driver, open_main_page, start_registration, fill_and_submit_registration_form,
                           redirection_to_my_profile):
    with allure.step("Open main page"):
        open_main_page()
    with allure.step("Start registration"):
        start_registration()
    with allure.step("Fill and submit registration form"):
        fill_and_submit_registration_form()

    with allure.step("Check for successful registration - user is redirected to My Profile page"):
        assert redirection_to_my_profile(), "User is not on the profile page after registration."
