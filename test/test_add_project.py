from project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_projects_list
    project = Project(project_name = "9")
    app.project.create(project)
    new_projects = app.project.get_projects_list()
  #  old_projects.append(project)
  #  assert old_projects == new_projects

    print(old_projects)
  #  print(new_projects)




