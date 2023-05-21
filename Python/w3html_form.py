# Use directory to fill details in form and switch to frame
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")
print(driver.title)
driver.maximize_window()
form_list = {"Novak": "Djokovic", "Rafael": "Nadal", "Roger": "Federer", "Pete": "Sampras", "Andre": "Agassi"}
for key, value in form_list.items():
    driver.find_element(By.XPATH, "//button[@id='runbtn']").click()
    frame = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
    driver.switch_to.frame(frame)
    fname = driver.find_element(By.ID, "fname")
    fname.clear()
    fname.send_keys(key)
    lname = driver.find_element(By.ID, "lname")
    lname.clear()
    lname.send_keys(value)
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    driver.switch_to.default_content()
    time.sleep(3)
