import copy

class Illness:
    def __init__(self, name, pathogen):
        self.name = name
        self.pathogen = copy.deepcopy(pathogen)

    def clinical_form(self):
        return next(cf for cf in self.pathogen.clinical_forms if cf.name == self.name)