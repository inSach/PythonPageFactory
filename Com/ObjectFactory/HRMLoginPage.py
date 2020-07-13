from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage_Objects(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {
        "otxt_uname": ('ID', 'txtUsername'),
        'otxt_pwd': ('ID', "txtPassword"),
        'obtn_login': ('ID', "btnLogin")
    }


class HomePage_Objects(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {
        'lnk_welcomeadmin': ('LINK_TEXT', "Welcome Admin"),
        'lnk_logout': ('LINK_TEXT', "Logout")
    }