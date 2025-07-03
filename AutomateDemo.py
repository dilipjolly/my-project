from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FormFillup:
    def registration(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/Register.html")
        driver.implicitly_wait(10)

        print("Page title is:", driver.title)

        # Basic Info
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Sameer")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Sharma")
        driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys("Puri Gate, B.R. Nagar, PIN-721306, Kharagpur, West Bengal")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("dilipjolly@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("8637060998")
        print("Personal details have been submitted")

        # Gender and Hobbies
        driver.find_element(By.XPATH, "//input[@value='Male']").click()
        driver.find_element(By.ID, "checkbox1").click()
        driver.find_element(By.ID, "checkbox2").click()
        driver.find_element(By.ID, "checkbox3").click()
        print("Hobbies selected")

        # Language selection
        driver.find_element(By.ID, "msdd").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li/a[text()='Hindi']"))).click()
        driver.find_element(By.XPATH, "//label[text()='Languages']").click()  # Click outside to close dropdown
        print("Language selected")

        # Skills
        skills_dropdown = Select(driver.find_element(By.ID, "Skills"))
        skills_dropdown.select_by_visible_text("Python")
        print("Skills selected")

        # Country selection
        driver.find_element(By.XPATH, "//span[@role='combobox']").click()
        driver.find_element(By.XPATH, "//li[text()='India']").click()
        print("Country selected")

        # DOB selection
        Select(driver.find_element(By.ID, "yearbox")).select_by_visible_text("1996")
        Select(driver.find_element(By.XPATH, "//select[@placeholder='Month']")).select_by_index(10)
        Select(driver.find_element(By.XPATH, "//select[@placeholder='Day']")).select_by_index(24)
        print("DOB selected")

        # Password
        driver.find_element(By.ID, "firstpassword").send_keys("Password")
        driver.find_element(By.ID, "secondpassword").send_keys("Password")

        # Alert Handling
        driver.find_element(By.XPATH, "//a[text()='SwitchTo']").click()
        driver.find_element(By.XPATH, "//a[text()='Alerts']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
        driver.switch_to.alert.accept()

        driver.find_element(By.XPATH, "//a[text()='Alert with OK & Cancel ']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        driver.switch_to.alert.dismiss()

        driver.find_element(By.LINK_TEXT, "Alert with Textbox").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
        driver.switch_to.alert.send_keys("Dilip")
        driver.switch_to.alert.accept()
        print("Alert textbox handled")

        # Windows Handling
        driver.find_element(By.XPATH, "//a[text()='SwitchTo']").click()
        driver.find_element(By.XPATH, "//a[text()='Windows']").click()
        driver.find_element(By.XPATH, "//a/button[@class='btn btn-info']").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        print("Switched to new window")
        # time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='Documentation']").click()
        driver.close()
        driver.switch_to.window(windows[0])
        # time.sleep()2

        # Date Picker
        driver.find_element(By.XPATH, "//a[text()='Widgets']").click()
        driver.find_element(By.XPATH, "//a[text()= ' Datepicker ']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@class = 'form-control is-datepick']").click()

        year = Select(driver.find_element(By.XPATH, "//select[@title= 'Change the year']"))
        time.sleep(3)
        year.select_by_visible_text("2024")
        time.sleep(3)
        month = Select(driver.find_element(By.XPATH, "//select[@title='Change the month']"))
        time.sleep(3)
        month.select_by_index(11)

        try:
            driver.find_element(By.XPATH, "//a[text()='31']").click()
        except:
            print("Date 31 not available in the selected month")

        driver.find_element(By.ID, "datepicker1").click()
        for _ in range(12):
            driver.find_element(By.XPATH, "//span[text()='Next']").click()
        driver.find_element(By.XPATH, "//a[text()='24']").click()
        time.sleep(5)

        print("Form Fillup Automation Completed")

        driver.quit()


# Run the automation
obj = FormFillup()
obj.registration()
