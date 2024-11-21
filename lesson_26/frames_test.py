"""
 Write a python selenium code that will go through two frames on the start page,
 navigate each frame, enter the correct secret text, click the “Verify” button,
 compare the text of the dialog box to confirm the success of the verification and close the dialog box
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://localhost:8000/dz.html"

driver = webdriver.Chrome()
driver.get(url)

try:
    # Finding and navigating to element frame 1
    frame_1 = driver.find_element(By.ID, "frame1")
    driver.switch_to.frame(frame_1)
    # Finding input field and sending text
    input_1 = driver.find_element(By.ID, "input1")
    input_1.send_keys("Frame1_Secret")
    # Finding verify button and clicking on it
    verify_btn1 = driver.find_element(By.CSS_SELECTOR, "input#input1 + button")
    verify_btn1.click()

    # Waiting until dialog window is present
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    # Comparing text
    assert alert.text == "Верифікація пройшла успішно!", "Перевірка неуспішна в першому фреймі!"
    alert.accept()

    # Navigate to main page
    driver.switch_to.default_content()

    # Finding and navigating to element frame 2
    frame2 = driver.find_element(By.ID, "frame2")
    driver.switch_to.frame(frame2)
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    button2 = driver.find_element(By.CSS_SELECTOR, "input#input2 + button")
    button2.click()

    # Waiting until dialog window is present
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "Верифікація пройшла успішно!", "Перевірка неуспішна в другому фреймі!"
    alert.accept()

    print("All checks have been successfully passed!")

finally:
    driver.quit()
