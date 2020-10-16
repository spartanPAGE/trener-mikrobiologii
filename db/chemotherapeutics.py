from models.Chemotherapeutic import Chemotherapeutic

chemotherapeutics_db = [
    Chemotherapeutic(
        name="linezolid",
        traits=["oksazolidyny"],
    ),
    Chemotherapeutic(
        name="lewofloksacyna",
        traits=["fluorochinolony"],
    ),
    Chemotherapeutic(
        name="moksifloksacyna",
        traits=["naftyrydynochinolony"],
    ),
    Chemotherapeutic(
        name="erytromycyna",
        traits=["makrolidy", "makrolidy starszej generacji"],
    ),
    Chemotherapeutic(
        name="azytromycyna",
        traits=["makrolidy", "makrolidy nowszej generacji"],
    ),
    Chemotherapeutic(
        name="roksytomycyna",
        traits=["makrolidy", "makrolidy nowszej generacji"],
    ),
    Chemotherapeutic(
        name="klarytromycyna",
        traits=["makrolidy", "makrolidy nowszej generacji"],
    ),
    Chemotherapeutic(
        name="josamycyna",
        traits=["makrolidy", "makrolidy nowszej generacji"],
    ),
    Chemotherapeutic(
        name="spiramycyna",
        traits=["makrolidy", "makrolidy nowszej generacji"],
    ),
    Chemotherapeutic("bacytracyna"),
    Chemotherapeutic("cefazolina"),
    Chemotherapeutic("wankomycyna"),
    Chemotherapeutic(
        name="penicylina benzylowa",
        traits=["penicyliny"]
    ),
    Chemotherapeutic(
        name="penicylina z inhibitorem beta-laktamazy",
        traits=["penicyliny"]
    ),
    Chemotherapeutic(
        name="kloksacylina",
    ),
    Chemotherapeutic(
        name="cefalosporyny 1 generacji",
        description="""
            działają silniej na bakterie Gram-dodatnie niż na Gram-ujemne.
            Są nieaktywne w stosunku do pałeczek G-: Pseudomonas aeruginosa, pałeczek salmonelli i bakterii z rodziny Proteus.
            Słabo przenikają do płynu mózgowo-rdzeniowego.
        """,
        traits=["cefalosporyny"],
    ),
    Chemotherapeutic(
        name="cefalosporyny 2 generacji",
        description="""
            działają silniej na bakterie Gram-dodatnie niż na Gram-ujemne.
            Są nieaktywne w stosunku do Pseudomonas aeruginosa ani Gram-ujemnych beztlenowców.
        """,
        traits=["cefalosporyny"],
    ),
    Chemotherapeutic(
        name="cefalosporyny 3 generacji",
        description="""
        Wykazują szerokie spektrum działania.
        są skuteczne w leczeniu zakażeń opornych na inne antybiotyki.
        Większość przechodzi przez barierę krew-mózg i jest skuteczna w leczeniu zapalenia opon mózgowych
        """,
        traits=["cefalosporyny", "szerokie spektrum", "dobre przenikanie bariery krew-mózg"],
    ),
    Chemotherapeutic(
        name="cefalosporyny 4 generacji",
        description="""
        Wykazują szerokie spektrum działania.
        są skuteczne w leczeniu zakażeń opornych na inne antybiotyki.
        Większość przechodzi przez barierę krew-mózg i jest skuteczna w leczeniu zapalenia opon mózgowych
        """,
        traits=["cefalosporyny", "szerokie spektrum", "świetne przenikanie bariery krew-mózg"],
    ),
    Chemotherapeutic(
        name="cefalosporyny 5 generacji",
        description="""
        Mają dużą biodostępność, przenikają do płynu mózgowo-rdzeniowego.
        Trzeba je podawać pozajelitowo (np. dożylnie).
        Działają na gronkowce metycylinooporne (MRSA/MRCNS) oporne na inne β-laktamy oraz część enterokoków (naturalnie opornych na inne cefalosporyny).
        """,
        traits=["cefalosporyny", "szerokie spektrum"],
    )
]