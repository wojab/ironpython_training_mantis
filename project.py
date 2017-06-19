
class Project:

    def __init__(self, project_name = None):
        self.project_name = project_name

    def __repr__(self):
        return "%s" % (self.project_name)

