from project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.project_name)


    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value = 'Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    projects_cache = None

    def get_projects_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.projects_cache =[]
            for row in wd.find_elements_by_css_selector("tbody"):
                cells = row.find_elements_by_tag_name("tr")
           #     cells = row.find_elements_by_xpath("//a[@class ='row-1']")
           #     cells = row.find_elements_by_css_selector("a[href^='https']")
           #     cells = row.find_elements_by_css_selector("tr[class*='row-1']")
                project_name = cells[0].text
                self.projects_cache.append(Project(project_name = project_name))
        return list(self.projects_cache)



    def delete_project(self):
        wd = self.app.wd
        self.open_projects_page()
        self.delete_first_project()

    def delete_first_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("tr.row-1 > td > a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()




