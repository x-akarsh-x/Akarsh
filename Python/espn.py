# Print the list of players who got out in the match
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Espn(unittest.TestCase):
    def setUp(self) -> None:
        global driver, wait
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 300)
        driver.get("https://www.espncricinfo.com")
        driver.maximize_window()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@title, 'Indian Premier League 2023')]"))).click()
        time.sleep(15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Not Now']"))).click()

    def test_ipl1(self):

        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Fixtures and Results')]"))).click()
        time.sleep(15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ds-p-0']//span[contains(text(),'RESULT')])["
                                                         "last()]/../../.."))).click()
        teams = {}
        for v in range(1, 3):
            t = wait.until(
                EC.element_to_be_clickable((By.XPATH, "((//div[contains(@class,'ds-grow')])[1]//span["
                                                      "contains(@class, 'ds-capitalize')])[" + str(v) + "]")))
            team = t.text
            if team not in teams:
                teams[team] = []
                for i in range(1, 4):
                    if i == 1 and v == 1:
                        out_players = wait.until(
                            EC.presence_of_all_elements_located((By.XPATH, "(//table)[" + str(
                                i) + "]//i[contains(@class, 'arrow_down')]/../../preceding-sibling::td/a")))
                        for player in out_players:
                            p = player.get_attribute("title")
                            teams[team].append(p)
                    elif i == 3 and v == 2:
                        out_players = wait.until(
                            EC.presence_of_all_elements_located((By.XPATH, "(//table)[" + str(
                                i) + "]//i[contains(@class, 'arrow_down')]/../../preceding-sibling::td/a")))
                        for player in out_players:
                            p = player.get_attribute("title")
                            teams[team].append(p)
                    else:
                        continue
        print(teams)
        keys = teams.keys()
        for i in keys:
            print("Out players of ", i, "is:")
            players = teams[i]
            for player in players:
                print(player)

    def test_ipl2(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()= 'Results']"))).click()
        time.sleep(15)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "((//div[@class='ds-block'])[2]//span[text()= 'RESULT'])[1]"))).click()
        teams = {}
        for v in range(1, 3):
            t = wait.until(
                EC.element_to_be_clickable((By.XPATH, "((//div[contains(@class,'ds-grow')])[1]//span["
                                                      "contains(@class, 'ds-capitalize')])[" + str(v) + "]")))
            team = t.text
            if team not in teams:
                teams[team] = []
                for i in range(1, 4):
                    if i == 1 and v == 1:
                        out_players = wait.until(
                            EC.presence_of_all_elements_located((By.XPATH, "(//table)[" + str(
                                i) + "]//i[contains(@class, 'arrow_down')]/../../preceding-sibling::td/a")))
                        for player in out_players:
                            p = player.get_attribute("title")
                            teams[team].append(p)
                    elif i == 3 and v == 2:
                        out_players = wait.until(
                            EC.presence_of_all_elements_located((By.XPATH, "(//table)[" + str(
                                i) + "]//i[contains(@class, 'arrow_down')]/../../preceding-sibling::td/a")))
                        for player in out_players:
                            p = player.get_attribute("title")
                            teams[team].append(p)
                    else:
                        continue
        keys = teams.keys()
        for i in keys:
            print("\nOut players of", i, "is:")
            players = teams[i]
            for player in players:
                print(player)

    def tearDown(self) -> None:
        driver.quit()
