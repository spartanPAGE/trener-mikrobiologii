import pprint

class ClinicalForm:
    def __init__(self, name, susceptibilities=[], requirements=[]):
        self.name = name
        self.susceptibilities = susceptibilities
        self.requirements = requirements

    def __repr__(self):
        return pprint.pformat(vars(self))
