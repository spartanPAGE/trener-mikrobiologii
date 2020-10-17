import copy

class Illness:
    def __init__(self, name, pathogen):
        self.name = name
        self.pathogen = copy.deepcopy(pathogen)