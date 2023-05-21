# Print the state office details of bjp
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import unittest


class Bjp(unittest.TestCase):
    def setUp(self) -> None:
        global driver, wait
        driver = webdriver.Edge()
        wait = WebDriverWait(driver, 300)
        driver.get("https://www.bjp.org")

    def test_StateWebsite(self):
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'State Websites'))).click()
        state = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[text()='Select State'])["
                                                                        "1]/following-sibling::select"))))
        states = wait.until(EC.presence_of_all_elements_located((By.XPATH, "(//label[text()='Select State'])["
                                                                           "1]/following-sibling::select/option")))
        for s in states:
            if "D" in s.text:
                state.select_by_visible_text(s.text)
                time.sleep(2)
                print("The state office details of", s.text, "are:")
                details = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, "//p[@class = 'c-detail-address']")))
                for detail in details:
                    if s.text in detail.text:
                        print(detail)
                    else:
                        continue
        bjp_title = driver.find_element(By.XPATH, '//title')
        self.assertTrue(driver.title == bjp_title.text)