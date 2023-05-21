# Go to enquiry form and fill the details
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver,35)
actions = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.iocl.com/")
print(driver.title)
iofu = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"IndianOil For You")))
actions.move_to_element(iofu).perform()
iofc = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"IndianOil for Careers")))
actions.move_to_element(iofc).perform()
lastest = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Latest Job Opening")))
actions.move_to_element(lastest).perform()
job = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Job Opening")))
actions.move_to_element(job).click().perform()
print(driver.current_url)
result = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Click Here to Check Your Final Result [31/01/2023]")))
actions.move_to_element(result).perform()

iofe = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"IndianOil for Environment")))
actions.move_to_element(iofe).perform()
satat = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"SATAT")))
actions.move_to_element(satat).perform()
enquiry = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Enquiry Form")))
actions.move_to_element(enquiry).click().perform()
print(driver.current_url)

name = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='SatatEnquiryFormdto_Name']")))
name.click()
name.send_keys("Test")
state = Select(driver.find_element(By.ID,"ddlstate"))
state.select_by_visible_text("Tamil Nadu")
firm = Select(driver.find_element(By.ID,"ddldistrict"))
firm.select_by_visible_text("Others")
num = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='txtMobileNo']")))
num.click()
num.send_keys("9876543210")
e_mail = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='txtEmail']")))
e_mail.click()
e_mail.send_keys("test@test.com")
turnover = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='txtAnnualTurnover']")))
turnover.click()
turnover.send_keys("20")
time.sleep(30)