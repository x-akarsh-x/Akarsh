# First change the language to hindi then back to english ,and second go through all faqs and click it
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Dream11(unittest.TestCase):

    def setUp(self) -> None:
        global driver, wait, actions
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        driver.get("https://www.dream11.com")
        driver.maximize_window()

    def test_A_goto(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='select-selected']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='hindi']"))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='select-selected']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='english']"))).click()
        time.sleep(3)

    def test_B_goto(self):
        i = 1
        while i < 9:
            if i == 8:
                move_to = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Download App")))
                actions.move_to_element(move_to).perform()
            else:
                move_to = wait.until(EC.element_to_be_clickable((By.ID, "accordion_" + str(i + 1) + "")))
                actions.move_to_element(move_to).perform()
            element = wait.until(EC.element_to_be_clickable((By.ID, "accordion_" + str(i) + "")))
            element.click()
            print(element.text)
            i += 1

    def tearDown(self) -> None:
        driver.quit()
