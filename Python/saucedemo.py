# Login to saucedemo, add 1st product to cart ,and use assertion to check visibility of error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class SauceDemo(unittest.TestCase):

    def test_demo(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 30)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        for u in users:
            user = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'Username']")))
            user.clear()
            user.send_keys(u)
            password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'Password']")))
            password.clear()
            password.send_keys("secret_sauce")
            wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
            if u == 'locked_out_user':
                continue
            else:
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, "(//div[@class='inventory_list']//button)[1]"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
                Error = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[@data-test = 'error']")))
                self.assertTrue(Error.text == 'Error: First Name is required')
                fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'First Name']")))
                fn.send_keys('Andrew')
                ln = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'Last Name']")))
                ln.send_keys('Baker')
                zip = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'Zip/Postal Code']")))
                zip.send_keys('90210')
                if Error.get_attribute('data-test') == 'error':
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@id,'logout')]"))).click()
                    continue
                else:
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))).click()
                    status = wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[@class = 'complete-header']")))
                    self.assertTrue(status.text == 'Thank you for your order!')
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='back-to-products']"))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']"))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@id,'logout')]"))).click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
