import pprint

class ClinicalForm:
    def __init__(self, name, susceptibilities=None, requirements=None, treatments=None):
        self.name = name
        self.susceptibilities = susceptibilities or []
        self.requirements = requirements or []
        self.treatments = treatments or []

    def __repr__(self):
        return pprint.pformat(vars(self))
