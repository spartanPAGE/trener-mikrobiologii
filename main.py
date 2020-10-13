import random
import pprint
import copy

from tools.clinical_forms_prep import extract_clinical_forms_by_susceptibilities
from tools.patients_prep import generate_sick_patient

from db.pathogens import pathogens_db
from db.patients import patients_db

# todo: handle requirements of clinical forms
if __name__ == "__main__":
    clinical_forms_db = extract_clinical_forms_by_susceptibilities(pathogens_db)
    
    for i in range(5):
        patient_model = random.choice(patients_db)
        sick_patient = generate_sick_patient(patient_model, pathogens_db, clinical_forms_db)
        print(sick_patient.age, sick_patient.sex, sick_patient.predispositions, sick_patient.pathogens[0].name, sick_patient.clinical_forms[0].name)
