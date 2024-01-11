from const.paths import FAMILIES_PATH

class FamilyClassifier:
    def __init__(self) -> None:
        self.data: list[Family] = []

        self.load_data(FAMILIES_PATH)
    
    def classify(self, species):
        for family in self.data:
            if species in family.members:
                return family.name
        else:
            return None

    def load_data(self, path):
        file = open(path, "r")
        raw_data = file.readlines()

        self.data = [self.convert_data(data) for data in raw_data]
    
    def convert_data(self, data):
        data = data.replace("\n", "")
        name, raw_members = data.split(":")
        members = raw_members.split(",")

        return Family(name, members)

class Family:
    def __init__(self, name, members) -> None:
        self.name = name
        self.members = members