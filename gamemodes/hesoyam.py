import random

from db.chemotherapeutics import chemotherapeutics_db
from db.lab_tests import lab_tests_db
from db.pathogens import pathogens_db
from db.patients import patients_db
from db.reactants import reactants_db

from tools.clinical_forms_prep import extract_clinical_forms_by_susceptibilities
from tools.patients_prep import generate_sick_patient

def prepare_clinical_forms_db():
    return extract_clinical_forms_by_susceptibilities(pathogens_db)

def prepare_patient(clinical_forms_db):
    patient_model = random.choice(patients_db)
    return generate_sick_patient(patient_model, pathogens_db, clinical_forms_db)

def hesoyam_gamemode():
    clinical_forms_db = prepare_clinical_forms_db()
    patient = prepare_patient(clinical_forms_db)

    print(patient.age, patient.sex, patient.predispositions, [cf.name for cf in patient.clinical_forms])