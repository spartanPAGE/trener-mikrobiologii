from models.Reagent import Reagent
from db.chemotherapeutics import chemotherapeutics_db

reagents_db = [
    Reagent("mannitol"),
    Reagent("krew"),
] + [Reagent(ch.name) for ch in chemotherapeutics_db]