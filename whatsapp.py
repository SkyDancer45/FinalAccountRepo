from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()

# open the webpage
driver.get("https://web.whatsapp.com/")
# sleep(200)
qrCode = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.TAG_NAME, "canvas")))
qr = qrCode.screenshot("cow.png")
sleep(30)
gridcell_elements = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@role='gridcell']"))
)

# Click on each gridcell and take a screenshot
for gridcell in gridcell_elements:
    gridcell.click()
    driver.save_screenshot(
        f"gridcell_{gridcell_elements.index(gridcell) + 1}.png")

driver.quit()
