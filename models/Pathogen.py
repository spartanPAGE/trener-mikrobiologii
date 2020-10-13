import pprint

class Pathogen:
    def __init__(self, name, clinical_forms=[]):
        self.name = name
        self.clinical_forms = clinical_forms

    def __repr__(self):
        return pprint.pformat(vars(self))
