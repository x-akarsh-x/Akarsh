# To verify image in every sections and get the page title of each section
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 15)
driver.get("https://www.americangolf.co.uk")
print(driver.title)
driver.maximize_window()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))).click()
href = []
images = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a/img[contains(@src,'/menu-images/')]")))
menu_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="a-level-1"]')))
club = wait.until(EC.element_to_be_clickable((By.XPATH, '(//a[@class="level-1 club-link a-level-1"])[2]')))
menu_list.append(club)
menu_list = menu_list[1:len(menu_list)]
count = len(menu_list)
for i in range(0, count):
    actions.move_to_element(menu_list[i]).perform()
    title = menu_list[i].text
    if wait.until(EC.element_to_be_clickable(images[i])):
        print("image is visible in ", title)
    elif wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'flyout-right'] /img[contains(@src,"
                                                          "'/menu-images/') and contains(@alt,'Golf Gifts')]"))):
        print("image is visible in ", title)
    else:
        print("image is not available in ", title)
    lst = menu_list[i].get_attribute("href")
    href.append(lst)
print(href)
for link in href:
    driver.get(link)
    print(driver.title)
time.sleep(15)
