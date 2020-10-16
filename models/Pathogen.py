class Treatment:
    def __init__(self, drug_name, success_chance=1.0):
        self.drug_name = drug_name
        self.success_chance = success_chance


class Pathogen:
    def __init__(self, name, clinical_forms=[], treatments=[], positive_tests=[], invitro_reactions=[]):
        self.name = name
        self.clinical_forms = clinical_forms
        self.treatments = treatments
        self.positive_tests = positive_tests
        self.invitro_reactions = invitro_reactions
