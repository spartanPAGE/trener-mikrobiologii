import random
import pprint
import copy

from models.PetriDish import PetriDish

from tools.clinical_forms_prep import extract_clinical_forms_by_susceptibilities
from tools.patients_prep import generate_sick_patient

from db.pathogens import pathogens_db
from db.patients import patients_db
from db.lab_tests import lab_tests_db
from db.chemotherapeutics import chemotherapeutics_db
from db.reactants import reactants_db


if __name__ == "__main__":
    clinical_forms_db = extract_clinical_forms_by_susceptibilities(pathogens_db)
    
    s_aureus = pathogens_db[0]

    petri_dishes = [
        PetriDish(
            name="agar z krwią i mannitolem",
            substances=["mannitol", "krew"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z samym mannitolem",
            substances=["mannitol"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z gównem",
            substances=["gówno"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z penicyliną benzylową",
            substances=["penicylina benzylowa"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z wankomycyną",
            substances=["wankomycyna"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z kloksacyliną",
            substances=["kloksacylina"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z cefazoliną",
            substances=["cefazolina"],
            pathogens=[s_aureus]
        ),
        PetriDish(
            name="agar z penicyliną z ihibitorem beta-laktamazy",
            substances=["penicylina z inhibitorem"],
            pathogens=[s_aureus]
        ),
    ]

    print("### Obserwacja S. aureus na pożywce agarowej z dodatkiem różnych substancji")

    for dish in petri_dishes:
        dish.react_to_time_passing()
        if len(dish.effects) > 0:
            print("Efekty szalki '", dish.name, "': ", dish.effects)
        else:
            print("Brak zmian w szalce '", dish.name, "'")


    patient_model = random.choice(patients_db)
    sick_patient = generate_sick_patient(patient_model, pathogens_db, clinical_forms_db)

    print("Dostępne terapeutyki: ")
    pprint.pprint(list([chemo.name for chemo in chemotherapeutics_db]))
    print("Dostępne testy:")
    pprint.pprint(list([test.name for test in lab_tests_db]))
    print("Dostępne reagenty:")
    pprint.pprint(list([r.name for r in reactants_db]))

    print("#" * 12)
    print("Wygenerowano pacjenta!")
    print("Wiek:", sick_patient.age)
    print("Płeć:", sick_patient.sex)
    print("Czynniki predyspozycyjne pacjenta: ")
    pprint.pprint(sick_patient.predispositions)
    print("Dolegliwości pacjenta: ")
    pprint.pprint(list([cf.name for cf in sick_patient.clinical_forms]))


