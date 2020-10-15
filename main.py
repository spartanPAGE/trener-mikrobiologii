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
from db.reagents import reagents_db

from gamemodes.hesoyam import hesoyam_gamemode

if __name__ == "__main__":
    hesoyam_gamemode()
