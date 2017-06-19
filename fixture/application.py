#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.android.webdriver import WebDriver
from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from selenium import webdriver

class Application:
    def __init__(self, browser="firefox", base_url="http://localhost/mantisbt-1.2.20"):
        if browser =="firefox":
           self.wd =webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError ("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url=base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

