
from db.chemotherapeutics import chemotherapeutics_db

def any_trait(substance, trait):
    for chemo in chemotherapeutics_db:
        if chemo.name == substance:
            return trait in chemo.traits
    return False

def does_substance_kills_pathogen(substance, pathogen):
    for treatment in pathogen.treatments:
        if substance == treatment.drug_name or any_trait(substance, treatment.drug_name):
            return True
    return False