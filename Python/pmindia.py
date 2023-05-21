# Print the former speakers of lok sabha
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
driver.get("https://www.pmindia.gov.in/en/")
print(driver.title)
time.sleep(2)

links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//i[@class = 'icon-external-link']")))
for link in links:
    try:
        link.click()
    except StaleElementReferenceException:
        break
time.sleep(2)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "Digital Sansad":
        break
time.sleep(2)
speaker = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 "
                                                           "HeaderIndividualCard_designationText__a_rR_ "
                                                           "mui-style-hywb98']")))
actions.move_to_element(speaker).perform()
profile = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text() =  'View Full Profile']")))
actions.move_to_element(profile)
actions.click()
actions.perform()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Former']"))).click()

lst = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//p[@class = 'MuiTypography-root "
                                                                  "MuiTypography-body1 style_memberName__Srgzp "
                                                                  "mui-style-sqip12']")))
for element in lst:
    var = element.text
    print(var)
