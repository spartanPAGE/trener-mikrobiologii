class Patient:
    def __init__(self, age, sex, predispositions=[], pathogens=[], clinical_forms=[]):
        self.age = age
        self.sex = sex
        self.predispositions = predispositions
        self.pathogens = pathogens
        self.clinical_forms = clinical_forms
