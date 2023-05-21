# To make list of links of every sections and go through it to print the page title
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 15)
driver.get("https://www.americangolf.co.uk")
print(driver.title)
driver.maximize_window()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))).click()
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'header-navigation-left']/ul/li/a")))
time.sleep(5)
menu_list = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'header-navigation-left']/ul/li/a")))
count = len(menu_list)
href = []
for i in range(0, count):
    actions.move_to_element(menu_list[i]).perform()
    if i >= 11 or "brands" in menu_list[i].get_attribute("href"):
        continue
    else:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[@class = 'header-navigation-left']/ul/li/a/..//img)[" + str(i + 1) + "]")))
    list = menu_list[i].get_attribute("href")
    href.append(list)
print(href)
for link in href:
    driver.get(link)
    print(driver.title)
time.sleep(15)
