# To select tomato and add to cart
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get("https://www.bigbasket.com")
catagory = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@qa = "categoryDD"]')))
catagory.click()
veggi = wait.until(EC.element_to_be_clickable((By.XPATH, '//ul[@id="navBarMegaNav"]/li[1]/a')))
veggi.click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='tab-content']//i[@class='fa fa-caret-down'])[6]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "((//div[@class='tab-content']//i[@class='fa fa-caret-down'])["
                                                 "6]/../..//a)[1]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Add'])[6]"))).click()
