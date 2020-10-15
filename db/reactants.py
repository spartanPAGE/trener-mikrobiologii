from models.Reactant import Reactant
from db.chemotherapeutics import chemotherapeutics_db

reactants_db = [
    Reactant("mannitol"),
    Reactant("krew"),
] + [Reactant(ch.name) for ch in chemotherapeutics_db]