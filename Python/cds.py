# Using Select and ActionChains class to select price low to high of "disc and usb packaging"
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.implicitly_wait(10)
driver.get("https://www.cds.com")
print(driver.title)
bottom = driver.find_element(By.XPATH, "//a[@title='FAQ/Help']")
allproducts = driver.find_element(By.XPATH, "//a[@title='All Products']")
actions.move_to_element(bottom).perform()
allproducts.click()
print(driver.current_url)
repair = driver.find_element(By.XPATH, "//a[@class='vnav__link' and text()='Repair Information']")
actions.move_to_element(repair).perform()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='vnav__link' and text()='Maintenance and Repairs'])[2]").click()
dayz = driver.find_element(By.XPATH, "//span[text()='30 Days.']")
print(dayz.text)
driver.find_element(By.XPATH, "//a[@class='vnav__link' and text()='Disc and USB Packaging']").click()
sort_by = Select(driver.find_element(By.ID, "SortBy"))
sort_by.select_by_visible_text("Price: Low to High")
time.sleep(30)
