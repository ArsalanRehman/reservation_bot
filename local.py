from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome WebDriver options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


#uncomment this line if you wanna run it locally 
webdriver_service = Service('/home/arslan/python_course/tenis/chromedriver')

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    driver.get("https://tenis.randevu.sanliurfa.bel.tr/index.php")
    
    # Give the page some time to load (increase sleep if needed)
    time.sleep(5)

    # Find all the <a> elements with the desired class
    elements = driver.find_elements(By.CSS_SELECTOR, "a.btn.btn-outline.btn-outline-dashed.btn-outline-success.btn-active-light-success.mb-2")

    # Iterate over the elements and click the one that says "15:00"
    for element in elements:
        if element.text == "15:00":
            element.click()
            print("Clicked the 15:00 court availability!")
            break
    else:
        print("No 15:00 time slot found.")
    
    # Give some time for the modal to appear
    time.sleep(2)

    confirm_button = driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm.swal2-styled.swal2-default-outline")
    confirm_button.click()
    print("Clicked the confirmation button on the modal!")

    time.sleep(5)

    driver.find_element(By.ID, "tc").send_keys("11111111111")
    driver.find_element(By.ID, "adi").send_keys("Arslan")
    driver.find_element(By.ID, "soyadi").send_keys("test soyadi")
    driver.find_element(By.ID, "cep_telefonu").send_keys("05431111111")
    driver.find_element(By.ID, "dogum_tarihi").send_keys("19/11/1998")

    gender_select = driver.find_element(By.ID, "cinsiyet")
    for option in gender_select.find_elements(By.TAG_NAME, 'option'):
        if option.text == "Erkek":
            option.click()
            break

    driver.find_element(By.ID, "konuk_dogum_tarihi").send_keys("20/11/1998")
    driver.find_element(By.ID, "konuk_tc").send_keys("11111111111")
    driver.find_element(By.ID, "konuk_adi").send_keys("test")
    driver.find_element(By.ID, "konuk_soyadi").send_keys("test surname")

    checkbox = driver.find_element(By.CLASS_NAME, "form-check-input")
    if not checkbox.is_selected():
        checkbox.click()

    print("Form filled and checkbox checked!")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-block.btn-primary")
    submit_button.click()
    print("Form submitted!")

    time.sleep(60)

finally:
    driver.quit()