class Animal:
    def __init__(self, properties, index, classifier) -> None:
        name, species, gender, age = properties

        self.id = index.generate_id()
        self.name = name
        self.species = species
        self.gender = gender
        self.group = classifier.classify(self.species)
        self.age = int(age)
    
    def str_data(self):
        base_lens= [3, 9, 9, 9, 2, 2]
        properties = [self.id, self.name, self.group, self.species, self.gender, self.age]
        spaces = [" " * (base_len - len(str(a_property))) for base_len, a_property in zip(base_lens, properties)]
        return f'|{self.id}{spaces[0]}|{self.name}{spaces[1]}|{self.group}{spaces[2]}|{self.species}{spaces[3]}|{self.gender}{spaces[4]}|{self.age}{spaces[5]}|'