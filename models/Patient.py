class Patient:
    def __init__(self, age, sex, predispositions=None, pathogens=None, illnesses=None):
        self.age = age
        self.sex = sex
        self.predispositions = predispositions or []
        self.pathogens = pathogens or []
        self.illnesses = illnesses or []
        
        self._apply_automatic_predispositions()

    def _apply_automatic_predispositions(self):
        if self.age < 1.0/12:
            self.predispositions.append("noworodek")
        elif self.age < 11:
            self.predispositions.append("dziecko")
        elif self.age < 18:
            self.predispositions.append("nastolatek")
        elif self.age < 60:
            self.predispositions.append("dorosły")
        else:
            self.predispositions.append("starzec")

        self.predispositions = list(set(self.predispositions))
