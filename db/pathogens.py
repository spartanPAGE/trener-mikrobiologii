from models.Pathogen import Pathogen, Treatment
from models.ClinicalForm import ClinicalForm
from models.InvitroReaction import InvitroReaction

S_PNEUMONIAE_SUS = [
    "przewlekła niewydolność krążeniowo-oddechowa",
    "upośledzenie śledziony",
    "brak śledziony",
    "cukrzyca",
    "niewydolność nerek",
    "hemodializa",
    "nowotwór",
    "HIV",
    "immunosupresja",
    "alkoholizm"
]

pathogens_db = [
    Pathogen(
        name="E. faecalis",
        clinical_forms=[
            # todo: add treatments for specific clinical forms (i.e. nitrofurantoin for urinary infection)
            ClinicalForm(
                name="ZUM",
                treatments=["ciprofloksacyna", "trometamol z fosfomycyną"]
            ),
            ClinicalForm("zapalenie wsierdzia"),
            ClinicalForm("zapalenie prostaty"),
            ClinicalForm("zapalenie najądrzy"),
        ],
        treatments=[
            Treatment("cefalosporyny 5 generacji"),
            Treatment("wankomycyna"),
            Treatment("ampicylina"),
            Treatment("teikoplanina"),
            Treatment("linezolid"),
            Treatment("penicyliny"),
        ],
        positive_tests=[
            "test PCR w kierunku GDS",
        ],
        invitro_reactions=[
            InvitroReaction("krew", "hemoliza gamma"),
            InvitroReaction("glukoza", "fermentacja bez gazu")
        ]
    ),
    Pathogen(
        name="S. pneumoniae",
        clinical_forms=[
            ClinicalForm(
                name="infekcja górnych dróg oddechowych",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="infekcja dolnych dróg oddechowych",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="zapalenie ucha środkowego",
                susceptibilities=S_PNEUMONIAE_SUS
            ),
            ClinicalForm(
                name="zapalenie zatok obocznych nosa",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="zapalenie oskrzeli",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="ropień opłucnej",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="ZOMR",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="spontaniczne zapalenie otrzewnej",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="zapalenie spojówek",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="zapalenie stawów",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="sepsa",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
            ClinicalForm(
                name="zapalenie płuc z bakteriemią, sepsą i ZOMR",
                susceptibilities=S_PNEUMONIAE_SUS,
            ),
        ],
        positive_tests=[
            "test antygenowy na wielocukier C",
        ],
        treatments=[
            Treatment("penicyliny"),
            Treatment("wankomycyna"),
            Treatment("linezolid"),
            Treatment("wankomycyna"),
            Treatment("lewofloksacyna"),
            Treatment("moksifloksacyna"),
            Treatment("teikoplanina"),
            Treatment("kloksacylina"),
            Treatment("cefalosporyny 2 generacji"),
            Treatment("cefalosporyny 3 generacji"),
            Treatment("cefalosporyny 4 generacji"),
            Treatment("cefalosporyny 5 generacji"),
        ],
        invitro_reactions=[
            InvitroReaction("krew", "hemoliza alfa"),
            InvitroReaction("optochina", "zachamowanie wzrostu"),
            InvitroReaction("żółć", "rozpuszczenie kolonii"),
        ],
    ),
    Pathogen(
        name="S. agalactiae",
        clinical_forms=[
            ClinicalForm("zapalenie płuc", susceptibilities=["noworodek", "alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("ZOMR", requirements=["noworodek"]),
            ClinicalForm("sepsa", susceptibilities=["noworodek", "alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("zakażenie pępka lub kikuta pępowiny", requirements=["noworodek"]),
            ClinicalForm("zapalenie ucha środkowego"),
            ClinicalForm("zapalenie kości, szpiku i stawów", susceptibilities=["ciężarna", "alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("zapalenie kosmówki", requirements="ciężarna"),
            ClinicalForm("ZUM", susceptibilities=["ciężarna", "alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("zapalenie błony śluzowej macicy", requirements=["niedawny poród"]),
            ClinicalForm("gorączka połodowa", requirements=["niedawny poród"]),
            ClinicalForm("zapalenie skóry i tkanek miękkich", susceptibilities=["alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("zapalenie gardła", susceptibilities=["alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("zapalenie wsierdzia", susceptibilities=["ciężarna", "alkoholizm", "starzec", "obniżona odporność"]),
            ClinicalForm("zapalenie otrzewnej", susceptibilities=["ciężarna", "alkoholizm", "starzec", "obniżona odporność"]),
        ],
        positive_tests=[
            "test na hemolizyny",
            "test antygenowy w kierunku S. agalactiae",
            "test na streptokinazę",
            "test PCR w kierunku GBS",
        ],
        treatments=[
            Treatment("wankomycyna"),
            Treatment("makrolidy"),
            Treatment("teikoplanina"),
            Treatment("penicyliny"),
            Treatment("cefalosporyny 1 generacji"),
            Treatment("cefalosporyny 3 generacji"),
            Treatment("cefalosporyny 4 generacji"),
            Treatment("cefalosporyny 5 generacji"),
        ],
        invitro_reactions=[
            InvitroReaction("krew", "hemoliza beta"),
        ]
    ),
    Pathogen(
        name="S. pyogenes",
        clinical_forms=[
            ClinicalForm("zapalenie gardła"),
            ClinicalForm("ostre zapalenie gardła i migdałków"),
            ClinicalForm("szkarlatyna"),
            ClinicalForm("zapalenie ucha"),
            ClinicalForm("zapalenie zatok"),
            ClinicalForm("zapalenie węzłów chłonnych"),
            ClinicalForm("róża"),
            ClinicalForm("liszajec"),
            ClinicalForm("ropień skórny"),
            ClinicalForm("celulitis"),
            ClinicalForm("zakażenie rany", susceptibilities=["rana"]),
            ClinicalForm("infekcja oparzenia", requirements=["oparzenie"]),
            ClinicalForm("zakażenie pępka lub kikuta pępowiny", susceptibilities=["noworodek"]),
            ClinicalForm("martwicze zapalenie powięzi"),
            ClinicalForm("sepsa"),
            ClinicalForm("zespół wstrząsu toksycznego"),
            ClinicalForm("zapalenie płuc"),
            ClinicalForm("ZOMR", requirements=["uraz"]),
            ClinicalForm("zapalenie wsierdzia"),
            ClinicalForm("zapalenie kości i szpiku"),
            ClinicalForm("rumień guzowaty"),
            ClinicalForm("ropień okołomigdałkowy"),
            ClinicalForm("ropień pozagardłowy"),
            ClinicalForm("gorączka reumatyczna", susceptibilities=["dziecko"]),
            ClinicalForm("kłębuszkowe zapalenie nerek", susceptibilities=["dziecko"]),
        ],
        positive_tests=[
            "test na białko M",
            "test na białko F",
            "test na białko G",
            "test na hialuronidazę",
            "test na streptokinazę",
            "test na proteinazę",
            "test na streptolizynę O",
            "test na streptolizynę S",
            "test na hemolizyny",
            "test na toksynę erytrogenną A (SpeA)",
            "test na toksynę erytrogenną B (SpeB)",
            "test na toksynę erytrogenną C (SpeC)",
            "test PCR w kierunku GAS",
        ],
        treatments=[
            Treatment("penicyliny"),
            Treatment("makrolidy"),
            Treatment("linkozamidy"),
            Treatment("cefalosporyny"),
            Treatment("bacytracyna"),
            Treatment("teikoplanina"),
        ],
        invitro_reactions=[
            InvitroReaction("krew", "hemoliza beta"),
        ],
    ),
    Pathogen(
        name="S. aureus",
        clinical_forms=[
            ClinicalForm("czyraczność"),
            ClinicalForm("czyrak", susceptibilities=["czyraczność"]),
            ClinicalForm("zapalenie mieszków włosowych", susceptibilities=["zła higiena", "czyraczność"]),
            ClinicalForm("jęczmień"),
            ClinicalForm("liszajec", susceptibilities=["zła higiena"]),
            ClinicalForm("zanokcica"),
            ClinicalForm("zastrzał"),
            ClinicalForm("ropne zapalenie gruczołów potowych"),
            ClinicalForm("zapalenie sutka", susceptibilities=["karmienie piersią"]),
            ClinicalForm("infekcja miejsca operowanego", requirements=["operacja"]),
            ClinicalForm("infekcja oparzenia", requirements=["oparzenie"]),
            ClinicalForm("infekcja odleżyny", requirements=["odleżyna"]),
            ClinicalForm("zapalenie płuc"),
            ClinicalForm("ropniak opłucnej", susceptibilities=["operacja"]),
            ClinicalForm("ZOMR", susceptibilities=["operacja", "uraz"]),
            ClinicalForm("ropień płuc", susceptibilities=["operacja"]),
            ClinicalForm("ropień nerek", susceptibilities=["operacja"]),
            ClinicalForm("ropień wątroby", susceptibilities=["operacja"]),
            ClinicalForm("ropień mózgu", susceptibilities=["ZOMR"]),
            ClinicalForm("ZUM", susceptibilities=["zła higiena"]),
            ClinicalForm("zapalenie ucha środkowego"),
            ClinicalForm("zapalenie zatok"),
            ClinicalForm("bakteriemia", susceptibilities=["obniżona odporność"]),
            ClinicalForm("sepsa", susceptibilities=["bakteriemia", "ciało obce", "obniżona odporność"]),
            ClinicalForm("zatrucie pokarmowe"),
            ClinicalForm("zespół poparzonej skóry"),
            ClinicalForm("zespół wstrząsu toksycznego", susceptibilities=["menstruacja"])
        ],
        treatments=[
            Treatment("kloksacylina"),
            Treatment("cefazolina"),
            Treatment("wankomycyna"),
            Treatment("penicylina z inhibitorem beta-laktamazy"),
            Treatment("ceftarolina"),
            Treatment("teikoplanina"),
            Treatment("cefalosporyny 1 generacji"),
            Treatment("cefalosporyny 3 generacji"),
            Treatment("cefalosporyny 4 generacji"),
            Treatment("cefalosporyny 5 generacji"),
        ],
        positive_tests=[
            "test na czynnik zlepny CF",
            "test na białko A",
            "test na polisacharyd otoczkowy S. aureus",
            "test na hialuronidazę",
            "test na stafylokinazę",
            "test na DN-azę",
            "test na proteinazę",
            "test na hemolizyny",
            "test na leukocydynę",
            "test na toksyny epidermolityczne: eksfoliatyny ETA, ETB",
            "test na enterotoksyny A-E",
            "test na TSST1",
            "test na katalazowy",
        ],
        invitro_reactions=[
            InvitroReaction("mannitol", "fermentacja"),
            InvitroReaction("krew", "hemoliza beta"),
        ]
    )
]
