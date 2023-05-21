# Get and print the current stocks of reliance
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 25)
driver.get("https://www.moneycontrol.com")
driver.maximize_window()
logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='https://images.moneycontrol.com/images"
                                                              "/common/headfoot/logo.png?impolicy=mchigh']")))
searchBox = driver.find_element(By.XPATH, "(//input[@id='search_str'])[1]")
searchBox.click()
searchBox.send_keys("RIL")
sug = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@id='form_topsearch']/div[@class = 'sugBox']/div["
                                                       "2]/ul/li/a[1]/span[1]")))
actions.move_to_element(sug).click().perform()
value = wait.until(EC.presence_of_element_located((By.ID, "nsecp")))
stock = value.get_attribute("rel")
print(stock)
time.sleep(20)
