class LabTest:
    def __init__(self, name, category="", traits=None, requirements=None):
        self.name = name
        self.category = category
        self.traits = traits or []
        self.requirements = requirements or []

    def perform_test(self, petri_dish):
        pathogens = petri_dish.pathogens
        for pathogen in pathogens:
            if  self.name in pathogen.positive_tests:
                return True
        return False
