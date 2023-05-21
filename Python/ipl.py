# Print match location, match dates, and results of matches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestIpl(unittest.TestCase):
    def setUp(self) -> None:
        global driver, wait
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 20)
        driver.get("https://www.iplt20.com/matches/schedule/men")

    def test_example(self):
        stadiums = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//li[@ng-repeat = 'list in fixLiveList']//p[@class = 'ng-binding']/span")))
        dates = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//li[@ng-repeat = 'list in fixLiveList']//div[@class ='vn-matchDate ng-binding']")))
        for statium in stadiums:
            print(statium.text)
        for date in dates:
            print(date.text)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "MATCHES"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "RESULTS"))).click()
        results = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//ul[@id='team_archive']//div[contains(@class, 'ticketTitle ')]")))
        for result in results:
            print(result.text)
        current_url = driver.find_element(By.XPATH, '//title')
        self.assertTrue(self, driver.title == current_url.text)

    def tearDown(self) -> None:
        driver.quit()


unittest.main(verbosity=2)
