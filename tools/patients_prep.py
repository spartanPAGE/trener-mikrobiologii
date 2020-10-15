import random
import copy

def _get_random_predisposed_form(patient_model, clinical_forms):
    random_predispositions = copy.copy(patient_model.predispositions)
    random.shuffle(random_predispositions)
    for predisposition in random_predispositions:
        if predisposition in clinical_forms:
            return clinical_forms[predisposition]
    return None

def _copy_clinical_forms_with_requirements(patient_model, mapped_cfs_with_pathogens):
    return [
        cf for cf in mapped_cfs_with_pathogens
        if set(cf['clinical_form'].requirements).issubset(patient_model.predispositions)
    ]

def _copy_susceptible_clinical_forms_with_requirements(patient_model, clinical_forms):
    result = {}
    for key, value in clinical_forms.items():
        result[key] = _copy_clinical_forms_with_requirements(patient_model, value)
    return result

def generate_sick_patient(patient_model, pathogens, clinical_forms):
    other_clinical_forms = _copy_clinical_forms_with_requirements(
        patient_model, clinical_forms["others"]
    )
    clinical_forms_by_susceptibility = _copy_susceptible_clinical_forms_with_requirements(
        patient_model, clinical_forms["by_susceptibility"]
    )
    container = other_clinical_forms

    if len(patient_model.predispositions) > 0 and random.random() > 0.5:
        container = _get_random_predisposed_form(
            patient_model, clinical_forms_by_susceptibility
        ) or other_clinical_forms

    cf_pathogen_dict = random.choice(container)
    pathogen_name = cf_pathogen_dict["pathogen"]
    clinical_form = cf_pathogen_dict["clinical_form"]

    pathogen = next(pathogen for pathogen in pathogens if pathogen.name == pathogen_name)
    patient = copy.deepcopy(patient_model)
    patient.pathogens.append(pathogen)

    patient.clinical_forms.append(clinical_form)

    return patient
