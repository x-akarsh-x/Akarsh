# Make directory to contain the links of all content types and print it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class Cocacola(unittest.TestCase):

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

    def test_A_run(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='searchIcon']/span"))).click()
        print(driver.current_url)
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='searchFilter__container']//button")))
        menu_items = []
        link_list = {}
        for i in range(1, 10):
            menu.click()
            media = driver.find_element(By.XPATH, "(//ul[@role='menu']/li/a)[" + str(i) + "]")
            menu_items.append(media.text)
            media.click()
            time.sleep(3)
            if "privacy-policy" in media.get_attribute("data-value"):
                continue
            else:
                results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div["
                                                                                    "@class='searchResult__results"
                                                                                    "-container']//a")))
                for item in menu_items:
                    if item not in link_list:
                        link_list[item] = []
                        for element in results:
                            link = element.get_attribute("href")
                            link_list[item].append(link)
        print(menu_items)
        print(link_list)
        for key, values in link_list.items():

            print("\nLinks in " + key + " is:\n")
            if key == "Policies":
                print("None")
            else:
                for value in values:
                    print(value)
