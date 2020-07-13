from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Com.ObjectFactory import HRMLoginPage


class HRM_MainPage():
    def login_HRM(self, driver):
        loginPage = HRMLoginPage.LoginPage_Objects(driver)
        # assert loginPage.otxt_uname.ID == "txtUsername"
        loginPage.otxt_uname.send_keys("Admin")
        loginPage.otxt_pwd.send_keys("admin123")
        loginPage.obtn_login.click()
        print("\\n this is form deepest bottom of my test")



    def logout_HRM(self, driver):
        homePage = HRMLoginPage.HomePage_Objects(driver)
        homePage.lnk_welcomeadmin.click()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        homePage.lnk_logout.click()
