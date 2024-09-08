from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# Specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()


# Open the webpage
driver.get("https://web.whatsapp.com/")

# Increased timeout for QR code visibility (adjust if needed)
qrCode = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.TAG_NAME, "canvas"))
)
qr = qrCode.screenshot("cow.png")

# Increased timeout for grid cell presence (adjust if needed)
sleep(30)
gridcell_elements = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//span[@class='x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1rg5ohu _ao3e']"))
)

# Desired substring to match
# Replace with your actual substring
desired_substring = "drugs"

# Click on each gridcell and take a screenshot if substring matches
for gridcell in gridcell_elements:
    gridcell.click()
    if desired_substring in gridcell.text:
        driver.save_screenshot(f"cow{gridcell_elements.index(gridcell)+1}.png")


driver.quit
