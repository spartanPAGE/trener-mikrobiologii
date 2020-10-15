class Chemotherapeutic:
    def __init__(self, name, description="", traits=None):
        self.name = name
        self.description = description
        self.traits = traits or []
