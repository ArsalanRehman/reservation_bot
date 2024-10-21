from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome WebDriver options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode, remove if you want to see the browser
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to ChromeDriver, adjust if necessary
webdriver_service = Service('/home/arslan/python_course/chromedriver')  

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    driver.get("https://tenis.randevu.sanliurfa.bel.tr/index.php?tarih=22/10/2024#")
    
    # Give the page some time to load (increase sleep if needed)
    time.sleep(5)

    # Find the buttons for available courts with the class for available spots
    available_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn-outline-success")

    # Iterate over the buttons and click the one after 18:00 if available
    for button in available_buttons:
        time_slot = button.text  # Assuming the button text contains the time slot like '18:00'
        if time_slot and "18:00" in time_slot:
            button.click()
            print("Court booked successfully!")
            break
    else:
        print("No available courts after 18:00 found.")

finally:
    # Close the WebDriver instance
    driver.quit()
