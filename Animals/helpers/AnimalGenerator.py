from structure.FamilyClassifier import FamilyClassifier
from const.paths import DATA_PATH
from structure.Animal import Animal
from const.text import NAMES
import random

class AnimalGenerator:
    def __init__(self, index) -> None:
        self.family_classifier = FamilyClassifier()
        self.index = index
        self.species = []

        self.get_species()

    def get_species(self):
        for family in self.family_classifier.data:
            self.species += family.members

    def generate(self, list_len):
        animals = [self.generate_random_animal() for i in range(list_len)]
        animals_data = [f'{a.name};{a.species};{a.gender};{a.age}\n' for a in animals]
        animals_str = ""
        for data in animals_data:
            animals_str += data

        file = open(DATA_PATH, "w")
        file.write(animals_str)
        file.close()

        self.index.data = animals
        self.index.temp_data = animals

    def generate_random_animal(self, name_len=8, max_age=10):
        name = random.choice(NAMES)
        species = random.choice(self.species)
        gender = random.choice(["m", "f"])
        age = random.randint(1, max_age)

        properties = [name, species, gender, age]
        return Animal(properties, self.index, self.family_classifier)