from project import Project


def test_add_project(app):
    # app.session.login("administrator", "root")
    # if len(app.project.get_projects_list()) == 0:
    #     app.project.create(Project(project_name="projekt_usuwany"))
    # app.project.delete_project()
    # lista = app.project.get_projects_list()
    # print(lista)
    app.session.login("administrator", "root")
    lista = app.project.get_projects_list()
    print(lista)


