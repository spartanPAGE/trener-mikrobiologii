class Chemotherapeutic:
    def __init__(self, name, description="", susceptible_pathogens=[], excluded_pathogens=[], traits=[]):
        self.name = name
        self.description = description
        self.susceptible_pathogens = susceptible_pathogens
        self.excluded_pathogens = excluded_pathogens
        self.traits = traits