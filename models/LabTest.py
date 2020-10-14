class LabTest:
    def __init__(self, name, category="", traits=[], requirements=[]):
        self.name = name
        self.category = category
        self.traits = traits
        self.requirements = requirements

    def perform_test(self, petri_dish):
        pathogens = petri_dish.pathogens
        for pathogen in pathogens:
            if  self.name in pathogen.positive_tests:
                return True
        return False
