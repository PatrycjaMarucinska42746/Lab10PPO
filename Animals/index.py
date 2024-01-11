from structure.AnimalIndex import AnimalIndex
from helpers.AnimalGenerator import AnimalGenerator
from structure.FamilyClassifier import FamilyClassifier
from structure.Panel import Panel
from const.paths import DATA_PATH

family_classifier = FamilyClassifier()
index = AnimalIndex(family_classifier)
index.load_file(DATA_PATH)

animal_generator = AnimalGenerator(index)

user_panel = Panel(index, animal_generator)
user_panel.run()