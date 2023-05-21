# Create Lead and then qualify it to opportunity
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest


class CustomerCreation(unittest.TestCase):

    def setUp(self) -> None:
        global driver, wait, actions
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 30)
        actions = ActionChains(driver)
        driver.get("https://org91296e38.crm8.dynamics.com/main.aspx")
        driver.maximize_window()
        time.sleep(4)
        email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='i0116']")))
        email.send_keys("pcubeworkforce@gmail.com")
        email.send_keys(Keys.RETURN)
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='i0118']")))
        password.send_keys("Salesforce")
        password.send_keys(Keys.RETURN)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='idSIButton9']"))).click()
        time.sleep(5)
        iframe = wait.until(EC.element_to_be_clickable((By.XPATH, "//iframe[@id='AppLandingPage']")))
        driver.switch_to.frame(iframe)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Dynamics 365 — custom']"))).click()
        driver.switch_to.default_content()

    def tearDown(self) -> None:
        driver.quit()

    def test_A_run(self):
        time.sleep(6)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button["
                                                         "@id='quickCreateLauncher_buttoncrm_header_global$button']"))).click()
        lead = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Lead']")))
        actions.move_to_element(lead).click().perform()
        for i in range(1, 9):
            detail = wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@id='quickCreateTabContainer']//input)[" + str(i + 1) + "]")))
            detail.clear()
            if i+1 == 8:
                time.sleep(2)
                detail.send_keys("test@gmail.com")
            else:
                time.sleep(2)
                detail.send_keys("100")
        purchase = Select(driver.find_element(By.XPATH, "//select[@aria-label='Purchase Timeframe']"))
        purchase.select_by_index(2)
        lead_source = Select(driver.find_element(By.XPATH, "//select[@aria-label='Lead Source']"))
        lead_source.select_by_index(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Save and Close']"))).click()
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='View Record']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Save & Close')]"))).click()
        time.sleep(5)

    def test_B_run(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leads']"))).click()
        filters = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Lead Filter by keyword']")))
        filters.click()
        filters.send_keys("100")
        filters.send_keys(Keys.RETURN)
        time.sleep(4)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ag-center-cols-container']//span)[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Qualify')]"))).click()
        time.sleep(4)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='opportunity|NoRelationship|Form|Mscrm.Form"
                                                         ".opportunity.Save.Menu$splitButtonId_button3$button']"))).click()
        saveandclose = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Save & Close']")))
        actions.move_to_element(saveandclose).click().perform()