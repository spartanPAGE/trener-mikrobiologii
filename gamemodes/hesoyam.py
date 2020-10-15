import random
import pprint

from db.chemotherapeutics import chemotherapeutics_db
from db.lab_tests import lab_tests_db
from db.pathogens import pathogens_db
from db.patients import patients_db
from db.reagents import reagents_db

from models.PetriDish import PetriDish

from tools.clinical_forms_prep import extract_clinical_forms_by_susceptibilities
from tools.patients_prep import generate_sick_patient

def prepare_clinical_forms_db():
    return extract_clinical_forms_by_susceptibilities(pathogens_db)

def prepare_patient(clinical_forms_db):
    patient_model = random.choice(patients_db)
    return generate_sick_patient(patient_model, pathogens_db, clinical_forms_db)

def show_patient_info(patient):
    print("Pacjent lat", patient.age, "płeć", "mężczyzna" if patient.sex == "M" else "kobieta")
    print("predyspozycje z wywiadu:", ", ".join(patient.predispositions))
    print("dolegliwości:", ", ".join([cf.name for cf in patient.clinical_forms]))

def show_available_chemo():
    print("dostępne leki:")
    print("\r\n".join(["  - " + ch.name for ch in chemotherapeutics_db]))

def show_available_tests():
    print("dostępne testy:")
    print("\r\n".join(["  - " + t.name for t in lab_tests_db]))

def show_available_reagents():
    print("dostępne odczynniki:")
    print("\r\n".join(["  - " + ch.name for ch in reagents_db]))

def input_in_range(text, range_):
    while True:
        result = input(text)
        if result.isnumeric() and int(result) in range_:
            return int(result)

class Game:
    def __init__(self):
        self.clinical_forms_db = prepare_clinical_forms_db()
        self.next_patient()
    
    def start(self):
        self.gameloop()

    def add_reagent_to_petri_dish(self, petri_dish):
        reagent_names = [r.name for r in reagents_db]
        reagent = ""
        while True:
            reagent = input("podaj reagent: ")
            if reagent in reagent_names:
                petri_dish.substances.append(reagent)
                return
            else:
                print("Nie ma takiego reagentu.")

    def prepare_petri_dish(self):
        petri_dish = PetriDish(
            name=input("opisz hodowlę: "),
            pathogens=self.patient.pathogens
        )
        
        show_available_reagents()
        actions = [
            ("wyjdź", exit),
            ("dodaj reagent", lambda: self.add_reagent_to_petri_dish(petri_dish)),
            ("przygotuj wymaz", lambda: None)
        ]
        while True:
            print("substancje w naczyniu hodowlanym:", petri_dish.substances)
            self.print_actions(actions)
            idx = self.get_decision_idx(actions)
            self.execute_action(idx, actions)

            if idx == len(actions)-1:
                break
        self.petri_dishes.append(petri_dish)

    def observe_petri_dishes(self):
        if len(self.petri_dishes) == 0:
            print("Brak hodowli do obserwacji.")
            return

        print("Obserwacje hodowli z wymazów pacjenta:")

        for dish in self.petri_dishes:
            dish.react_to_time_passing()
            effects_desc = "brak zmian" if len(dish.effects) == 0 else ", ".join(dish.effects)
            print(" - {} ---> {}".format(dish.name, effects_desc))

    def petri_dishes_action(self):
        if len(self.petri_dishes) > 0:
            print(", ".join([pd.name for pd in self.petri_dishes]))
        else:
            print("Brak przygotowanych hodowli.")

        actions = [
            ("wyjdź", exit),
            ("przygotuj hodowlę z wymazu", lambda: self.prepare_petri_dish()),
            ("zaobserwuj zmiany w hodowlach", lambda: self.observe_petri_dishes()),
            ("powrót", lambda: None)
        ]
        self.print_actions(actions)
        self.execute_action(self.get_decision_idx(actions), actions)

    def perform_lab_test(self):
        if len(self.petri_dishes) > 0:
            print("Możliwe do użycia hodowle:", end=" ")
            print(", ".join([pd.name for pd in self.petri_dishes]))
        else:
            print("Brak przygotowanych hodowli.")
            return

        tests = [test.name for test in lab_tests_db]
        test = None
        while True:
            test_name = input("Podaj nazwę testu: ")
            if test_name in tests:
                test = next(t for t in lab_tests_db if t.name == test_name)
                break

        dishes = [dish.name for dish in self.petri_dishes]
        dish = None
        while True:
            dish_name = input("Podaj nazwę hodowli: ")
            if dish_name in dishes:
                dish = next(d for d in self.petri_dishes if d.name == dish_name)
                break

        print(test.name, "wynik", ("POZYTYWNY" if test.perform_test(dish) else "NEGATYWNY"))

    def lab_tests_action(self):
        show_available_tests()
        actions = [
            ("wyjdź", exit),
            ("wykonaj test", lambda: self.perform_lab_test()),
            ("powrót", lambda: None)
        ]
        self.print_actions(actions)
        self.execute_action(self.get_decision_idx(actions), actions)

    def next_patient(self):
        self.patient = prepare_patient(self.clinical_forms_db)
        self.petri_dishes = []
        show_patient_info(self.patient)

    def print_actions(self, actions):
        print()
        print("### podejmij akcję: ", end="")
        for idx, action in enumerate(actions):
            print("[{}. {}]".format(idx, action[0]), end=" ")
        print()

    def get_decision_idx(self, actions):
        result = input_in_range(" >> wybór akcji: ", range(len(actions)))
        print("*" * 24)
        return result

    def execute_action(self, idx, actions):
        (_, functor) = actions[idx]
        functor()
        
    def gameloop(self):
        actions = [
            ("wyjdź", exit),
            ("o pacjencie", lambda: show_patient_info(self.patient)),
            ("leki", show_available_chemo),
            ("testy", lambda: self.lab_tests_action()),
            ("odczynniki do hodowli", show_available_reagents),
            ("hodowle", lambda: self.petri_dishes_action()),
            ("wypisz pacjenta", lambda: self.next_patient())
        ]

        while True:
            self.print_actions(actions)
            self.execute_action(self.get_decision_idx(actions), actions)

def hesoyam_gamemode():
    game = Game()
    game.start()
