class Bed:
    def __init__(self, patient = None, pathogens=None):
        self.patient = patient
        self.pathogens = pathogens or []

    def has_patient(self):
        return self.patient != None

    def is_free(self):
        return not self.has_patient()
