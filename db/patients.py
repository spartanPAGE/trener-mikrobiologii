from models.Patient import Patient

patients_db = [
    Patient(
        age=35,
        sex="K",
        predispositions=[
            "alkoholizm",
            "menstruacja",
            "pominięte szczepienie DTaP/DiPerTE",
        ]
    ),
    Patient(
        age=25,
        sex="M",
        predispositions=[
            "operacja"
        ]
    ),
    Patient(
        age=75,
        sex="M",
        predispositions=[
            "odleżyna",
            "alkoholizm"
        ]
    ),
    Patient(
        age=21,
        sex="K",
        predispositions=[
            "zła higiena",
            "pominięte szczepienie DTaP/DiPerTE",
        ]
    ),
    Patient(
        age=25,
        sex="K",
        predispositions=[
            "menstruacja"
        ]
    ),
    Patient(
        age=60,
        sex="K",
    ),
    Patient(
        age=65,
        sex="M",
    ),
    Patient(
        age=27,
        sex="M",
        predispositions=[
            "pominięte szczepienie DTaP/DiPerTE",
        ]
    )
]