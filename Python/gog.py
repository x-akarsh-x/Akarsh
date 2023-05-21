# Select the first game of store and discount ,and add to cart
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 25)
actions = ActionChains(driver)
driver.get("https://www.gog.com/")
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text() = "Store" and @hook-test]'))).click()
print(driver.current_url)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@selenium-id = "listButton"]'))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@selenium-id  = "gridButton"]'))).click()
hover_element = driver.find_element(By.XPATH, "(//div[@class='product-tile__info'])[1]")
actions.move_to_element(hover_element).perform()
time.sleep(2)
click_element = driver.find_element(By.XPATH, '//span[@class="add-to-cart__icon icon-gog-cart ng-star-inserted"]')
driver.execute_script("arguments[0].click();", click_element)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'menu__logo-icon'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Last chance!')]"))).click()
time.sleep(2)
print(driver.current_url)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'SHOW ME THE DISCOUNTS!')]"))).click()
hover_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//paginated-products-grid/div/product-tile/a/div[2]')))
actions.move_to_element(hover_element).perform()
time.sleep(2)
click_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button-primary add-to-cart"]')))
driver.execute_script("arguments[0].click();", click_element)
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@hook-test = "cartCounter"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@hook-test = "cartCheckoutNow"]'))).click()
