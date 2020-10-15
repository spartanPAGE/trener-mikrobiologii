import pprint

class ClinicalForm:
    def __init__(self, name, susceptibilities=None, requirements=None):
        self.name = name
        self.susceptibilities = susceptibilities or []
        self.requirements = requirements or []

    def __repr__(self):
        return pprint.pformat(vars(self))
