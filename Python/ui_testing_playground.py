# Get element from table and  print it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
cpu = True
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get("http://uitestingplayground.com/dynamictable")
chrome = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Chrome']")))
tabs = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[text()='Chrome']/following-sibling :: span")))
for tab in tabs:
    var = tab.text
    if "%" in var:
        cpu = var
    else:
        continue
cpu = "Chrome CPU: " + cpu
compare_cpu = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='bg-warning']")))
vir = compare_cpu.text
if cpu == vir:
    print("Cpu status in task manager", cpu, "is same as in yellow box", vir)
else:
    print("Cpu status in task manager", cpu, "is not same as in yellow box", vir)
