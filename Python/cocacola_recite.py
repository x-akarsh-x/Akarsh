# Verify the audio description in recite settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class CocacolaRecite(unittest.TestCase):

    def setUp(self) -> None:
        global driver, wait, actions
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)
        driver.get("https://www.coca-colacompany.com/home")
        driver.maximize_window()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Confirm my Choices'])[1]"))).click()

    def tearDown(self) -> None:
        driver.quit()

    def test_run(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='recitemeIcon']/span"))).click()
        time.sleep(5)
        menu_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class,"
                                                                              "'cmp-navigation__group')]//a")))
        for element in menu_list:
            actions.move_to_element(element).perform()
            time.sleep(5)
