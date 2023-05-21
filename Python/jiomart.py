# Store top 5 highest priced chairs in directory with item title and its price
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get("https://www.jiomart.com/?gclid"
           "=Cj0KCQjwxYOiBhC9ARIsANiEIfZxi_ApRY29S64KN2znHgRQQqbqA6_K0EVfVsNGGZ_xzW7wI_03DQUaAifvEALw_wcB")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_ham_menu']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Shop By Category']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//section[@class='all-category-page container-mh jm-mb-m']/div["
                                                 "11]/div/div)[1]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//section[@class='all-category-page container-mh jm-mb-m']/div["
                                                 "11]/div/div)[8]/div/div"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//section[@class='all-category-page container-mh jm-mb-m']/div["
                                                 "11]/div/div)[8]/div[2]/a"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='jm-body-xs']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='slider round'])[2]"))).click()
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='plp-card-details-wrapper']")))
time.sleep(5)
details = {}
for i in range(1, 6):
    nam = driver.find_element(By.XPATH, "(//div[@class='plp-card-details-wrapper'])[" + str(i) + "]/div/div[contains("
                                                                                                 "@class,"
                                                                                                 "'details-name')]")
    name = nam.text
    p = driver.find_element(By.XPATH, "(//div[@class='plp-card-details-wrapper'])[" + str(i) + "]/div/div[contains("
                                                                                               "@class,"
                                                                                               "'details-name"
                                                                                               "')]/following::div/div"
                                                                                               "/span[contains(@class,"
                                                                                               "'heading')]")
    price = p.text
    details[name] = price
print(details)
href = []
updated_details = {}
for key, value in details.items():
    chair = driver.find_element(By.XPATH, "//a[contains(@title,'" + str(key) + "')]")
    link = chair.get_attribute("href")
    driver.get(link)
    article = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='jm-body-s-bold jm-mr-xxs']/span")))
    i_d = article.text
    updated_details[i_d] = details[key]
    driver.back()
    driver.refresh()
    time.sleep(4)
print(updated_details)