import unittest
from selenium import webdriver
from Com.Common.BrowserHandler import BrowserHandler
from Src.BasicFunctions import HRM_MainPage
from unittest_data_provider import data_provider


class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C://InstallablePackages//PyDrivers//chromedriver.exe")
        cls.driver.maximize_window()
        print("\n This is from class Setup method")

    def setUp(self):
         print("\n Next test is ", self._testMethodName)

    dataSet = lambda:(
        "Data1", "Data2", "Data3"
    )

    @data_provider(dataSet)
    def test_login(self, data):
        print(data)
        driver = self.driver
        BrowserHandler().launch_URL(driver, "https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.assertTrue(True, "Test assertion")
        HRM_MainPage().login_HRM(driver)
        self.assertEqual(driver.title, "OrangeHRM", "Title is not matching")

    def test_logout(self):
        driver = self.driver
        HRM_MainPage().logout_HRM(driver)
        self.assertEqual(driver.title, "OrangeHRM", "Title is not matching")


    @classmethod
    def tearDownClass(cls):
        BrowserHandler().close_browser(cls.driver)


class MLoginTestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C://InstallablePackages//PyDrivers//chromedriver.exe")
        cls.driver.maximize_window()


    def test_login1(self):
        driver = self.driver
        BrowserHandler().launch_URL(driver, "https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        with self.subTest():
            self.assertTrue(True, "Test assertion")
        HRM_MainPage().login_HRM(driver)
        self.assertEqual(driver.title, "OrangeHRM", "Title is not matching")


    def test_logout1(self):
        driver = self.driver
        HRM_MainPage().logout_HRM(driver)
        self.assertEqual(driver.title, "OrangeHRM", "Title is not matching")


    @classmethod
    def tearDownClass(cls):
        BrowserHandler().close_browser(cls.driver)


# if __name__ == '__main__':
#     # HtmlTestRunner.main()
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users//buchusac//PycharmProjects//TestProjPageFactory//Reports//'))
