from tools.pathogen import does_substance_kills_pathogen

class PetriDish:
    def __init__(self, name, substances=None, pathogens=None):
        self.name = name
        self.substances = substances or []
        self.pathogens = pathogens or []
        self.effects = set()
        # todo: let substances kill pathogens

    def react_to_time_passing(self):
        self.react_based_on_invitro_reactions()
        self.react_based_on_treatments()

    def react_based_on_invitro_reactions(self):
        for substance in self.substances:
            for pathogen in self.pathogens:
                for pathogen_invitro_reaction in pathogen.invitro_reactions:
                    if substance == pathogen_invitro_reaction.substance:
                        self.effects.add(pathogen_invitro_reaction.effect)

    def react_based_on_treatments(self):
        for substance in self.substances:
            for pathogen in self.pathogens:
                if does_substance_kills_pathogen(substance, pathogen):
                        self.effects.add("śmierć patogenu")
