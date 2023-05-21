# Verify action_chains's drag and drop, click and hold, and move to offset ,and switching to frame
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 25)
driver.maximize_window()
driver.get("https://jqueryui.com")
drop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Droppable")))
drop.click()
drop_frame = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "demo-frame")))
driver.switch_to.frame(drop_frame)
drag = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Drag me to my target']")))
dropp = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='droppable']")))
time.sleep(4)
actions.drag_and_drop(drag, dropp).perform()
time.sleep(4)
driver.switch_to.default_content()
resize = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Resizable")))
resize.click()
driver.switch_to.frame(0)
icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon "
                                                        "ui-icon-gripsmall-diagonal-se']")))
actions.click_and_hold(icon).move_by_offset(-50, -55).release(icon).perform()
time.sleep(20)
