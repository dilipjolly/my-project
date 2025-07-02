# print("Isha")
# c = "Isha"
# for i in range(1,14):
#     print(i,c)

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time


def test_login():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/dilip/Downloads/staticwebpage/index.html")
    driver.title
    print(driver.title)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID, 'username').send_keys("Sameer Sharma")
    driver.find_element(By.ID, 'email').send_keys("dilip@gmail.com")
    time.sleep(5)


test_login()

# findlements - click all the radio button in sequence with time gap of 3 seconds
