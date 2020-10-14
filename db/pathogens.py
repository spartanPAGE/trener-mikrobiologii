from models.Pathogen import Pathogen, Treatment
from models.ClinicalForm import ClinicalForm
from models.InvitroReaction import InvitroReaction

pathogens_db = [
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
            Treatment("penicylina z inhibitorem beta-laktamazy")
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
        ],
        invitro_reactions=[
            InvitroReaction("mannitol", "fermentacja"),
            InvitroReaction("krew", "hemoliza"),
        ]
    )
]
