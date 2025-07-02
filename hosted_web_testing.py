from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains as AC


class ActionChain:
    pass


class Form_fillup:
    def registration(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.automationtesting.in/Register.html")

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.title
        print("The page title is", driver.title)

        driver.find_element(By.XPATH, "//input[@placeholder= 'First Name']").send_keys("Sameer")

        driver.find_element(By.XPATH, "//input[@placeholder= 'Last Name']").send_keys("Sharma")

        address = driver.find_element(By.XPATH, "//textarea[@class= 'form-control ng-pristine ng-untouched ng-valid']")
        address.send_keys("Puri Gate, B.R. Nagar, PIN- 721306, Kharagpur, West Bengal")

        driver.find_element(By.XPATH, "//input[@type= 'email']").send_keys("dilipjolly@gmail.com")

        driver.find_element(By.XPATH, "//input[@type= 'tel']").send_keys("8637060998")
        print("Personal details has been submitted")

        driver.find_element(By.XPATH, "//input[@type= 'radio']").click()

        driver.find_element(By.ID, "checkbox1").click()

        driver.find_element(By.ID, "checkbox2").click()

        driver.find_element(By.ID, "checkbox3").click()
        print("Hobbies has been selected")

        driver.find_element(By.ID, "msdd").click()

        driver.find_element(By.XPATH, "//li/a[text()='Hindi']").click()

        driver.find_element(By.ID, 'section').click()
        print("Language has been selected")

        select_skills = Select(driver.find_element(By.XPATH, "//select[@id = 'Skills']"))
        select_skills.select_by_visible_text("Python")

        print("Skills are set")

        driver.find_element(By.XPATH, "//span[@role='combobox']").click()

        driver.find_element(By.XPATH, "//li[text()='India']").click()
        print("Country has been selected")

        select_year = Select(driver.find_element(By.XPATH, "//select[@id = 'yearbox']"))
        select_year.select_by_visible_text("1996")

        select_month = Select(driver.find_element(By.XPATH, "//select[@placeholder = 'Month']"))
        select_month.select_by_index(10)

        select_month = Select(driver.find_element(By.XPATH, "//select[@placeholder = 'Day']"))
        select_month.select_by_index(24)

        print("DOB has been submitted")

        driver.find_element(By.ID, "firstpassword").send_keys("Password")

        driver.find_element(By.ID, "secondpassword").send_keys("Password")

        driver.find_element(By.XPATH, "//a[text() = 'SwitchTo']").click()

        driver.find_element(By.XPATH, "//a[text() = 'Alerts']").click()

        driver.find_element(By.XPATH, "//button[@class = 'btn btn-danger']").click()

        driver.switch_to.alert.accept()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()

        driver.find_element(By.XPATH, "//button[@class = 'btn btn-primary']").click()

        driver.switch_to.alert.dismiss()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Alert with Textbox").click()

        driver.find_element(By.XPATH, "//button[@class = 'btn btn-info']").click()

        driver.switch_to.alert.send_keys("Dilip")

        print("Name is asserted to alert")

        driver.switch_to.alert.accept()

        driver.find_element(By.XPATH, "//li//a[text()= 'SwitchTo']").click()

        driver.find_element(By.XPATH, "//li//a[text()= 'Windows']").click()

        driver.find_element(By.XPATH, "//a/button[(@class= 'btn btn-info')]").click()

        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        print("switch to window is done")
        driver.find_element(By.XPATH, "//div/ul/li/a/span[text() = 'Documentation']").click()

        time.sleep(2)
        driver.close()
        driver.switch_to.window(windows[0])

        element = driver.find_element(By.XPATH, "//a[text() = 'Widgets']")
        hover = AC(driver)
        hover.move_to_element(element).perform()

        driver.find_element(By.XPATH, "//a[text() = ' Datepicker ']").click()

        year_xpath = "//select[@title= 'Change the year']"
        year_locator = Select(driver.find_element(By.XPATH, year_xpath))

        year_locator.select_by_visible_text("2024")

        month_select = Select(driver.find_element(By.XPATH, "//select[@title= 'Change the month']"))
        month_select.select_by_index(11)

        driver.find_element(By.XPATH, "//a[text()= '31']").click()
        driver.find_element(By.ID, 'datepicker1').click()

        for _ in range(12):
            driver.find_element(By.XPATH, "//span[text()= 'Prev']").click()

        driver.find_element(By.XPATH, "//a[text()= '2']").click()

        driver.close()


#
obj = Form_fillup()
obj.registration()
