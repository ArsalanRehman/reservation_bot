import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome WebDriver options for Docker environment
chrome_options = Options()

# Ensure Chrome runs in headless mode
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer (optional)
chrome_options.add_argument("--remote-debugging-port=9222")  # Fix for DevToolsActivePort error
chrome_options.add_argument("--window-size=1920x1080")  # Set a fixed window size for headless mode

# Path inside Docker container
webdriver_service = Service('/usr/local/bin/chromedriver-linux64/chromedriver')

# Initialize the WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # Open the target URL
    driver.get("https://tenis.randevu.sanliurfa.bel.tr/index.php?tarih=23/10/2024")
    
    # Wait for the page to load
    time.sleep(5)

    # Find all the elements with the desired class
    elements = driver.find_elements_by_css_selector("a.btn.btn-outline.btn-outline-dashed.btn-outline-success.btn-active-light-success.mb-2")

    # Iterate over the elements and click the one that says "15:00"
    for element in elements:
        if element.text == "15:00":
            element.click()
            print("Clicked the 15:00 court availability!")
            break
    else:
        print("No 15:00 time slot found.")
    
    # Wait for the modal to appear
    time.sleep(2)

    # Click the confirmation button on the modal
    confirm_button = driver.find_element_by_css_selector("button.swal2-confirm.swal2-styled.swal2-default-outline")
    confirm_button.click()
    print("Clicked the confirmation button on the modal!")

    # Wait for the page to load the form
    time.sleep(5)

    # Fill in the form
    driver.find_element_by_id("tc").send_keys("11111111111")
    driver.find_element_by_id("adi").send_keys("Arslan")
    driver.find_element_by_id("soyadi").send_keys("test soyadi")
    driver.find_element_by_id("cep_telefonu").send_keys("05431111111")
    driver.find_element_by_id("dogum_tarihi").send_keys("19/11/1998")

    # Select gender
    gender_select = driver.find_element_by_id("cinsiyet")
    for option in gender_select.find_elements_by_tag_name('option'):
        if option.text == "Erkek":
            option.click()
            break

    # Fill in guest details
    driver.find_element_by_id("konuk_dogum_tarihi").send_keys("20/11/1998")
    driver.find_element_by_id("konuk_tc").send_keys("11111111111")
    driver.find_element_by_id("konuk_adi").send_keys("test")
    driver.find_element_by_id("konuk_soyadi").send_keys("test surname")

    # Check the checkbox if not already checked
    checkbox = driver.find_element_by_class_name("form-check-input")
    if not checkbox.is_selected():
        checkbox.click()

    print("Form filled and checkbox checked!")

    # Submit the form
    submit_button = driver.find_element_by_css_selector("button.btn.btn-block.btn-primary")
    submit_button.click()
    print("Form submitted!")

    # Wait for the form submission to complete
    time.sleep(60)

finally:
    # Always close the driver at the end
    driver.quit()
