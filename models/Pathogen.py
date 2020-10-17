class Treatment:
    def __init__(self, drug_name, success_chance=1.0):
        self.drug_name = drug_name
        self.success_chance = success_chance


class Pathogen:
    def __init__(
        self,
        name,
        clinical_forms=None,
        treatments=None,
        positive_tests=None,
        invitro_reactions=None,
    ):
        self.name = name
        self.clinical_forms = clinical_forms or []
        self.treatments = treatments or []
        self.positive_tests = positive_tests or []
        self.invitro_reactions = invitro_reactions or []
