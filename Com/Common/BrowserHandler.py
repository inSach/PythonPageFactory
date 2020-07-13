from selenium import webdriver

class BrowserHandler():
    def launch_URL(self, driver, url):
        driver.get(url)


    def close_browser(self, driver):
        driver.close()

