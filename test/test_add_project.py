from project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.create()
