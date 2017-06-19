from project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value = 'Create New Project']").click()

    def add_values(self):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys("abababa")

    def create(self):
        wd = self.app.wd
        self.open_projects_page()
        self.add_values()
        wd.find_element_by_xpath("//input[@value='Add Project']").click()



