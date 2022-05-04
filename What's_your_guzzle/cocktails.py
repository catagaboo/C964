# Package class creates package objects
class Cocktails:
    def __init__(self, name, glass, main_alcohol, other_alcohol, mixes, garnishes):
        self.name = name
        self.glass = glass
        self.main_alcohol = main_alcohol
        self.other_alcohol = other_alcohol
        self.mixes = mixes
        self.garnishes = garnishes
