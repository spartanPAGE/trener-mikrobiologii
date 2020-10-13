import random
import copy

def generate_sick_patient(patient_model, pathogens, clinical_forms):
    container = clinical_forms["others"]

    if len(patient_model.predispositions) > 0 and random.random() > 0.3:
        random_predispositions = copy.copy(patient_model.predispositions)
        for predisposition in random_predispositions:
            if predisposition in clinical_forms["by_susceptibility"]:
                container = clinical_forms["by_susceptibility"][predisposition]
                break

    cf_pathogen_dict = random.choice(container)
    pathogen_name = cf_pathogen_dict["pathogen"]
    clinical_form = cf_pathogen_dict["clinical_form"]

    pathogen = next(pathogen for pathogen in pathogens if pathogen.name == pathogen_name)
    patient = copy.deepcopy(patient_model)
    patient.pathogens.append(pathogen)

    patient.clinical_forms.append(clinical_form)

    return patient
