from models.Chemotherapeutic import Chemotherapeutic
from models.Illness import Illness
from models.Pathogen import Pathogen

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

def does_substance_treat_illness(
    substance: str,
    illness: Illness) -> bool:

    clinical_form = illness.clinical_form()
    if len(clinical_form.treatments) > 0:
        for treatment in clinical_form.treatments:
            if substance == treatment.drug_name or any_trait(substance, treatment.drug_name):
                return True
    else:
        return does_substance_kills_pathogen(substance, illness.pathogen)
