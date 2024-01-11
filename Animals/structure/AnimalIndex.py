from structure.Animal import Animal
from const.text import FILTER_TYPES, ERRORS
from helpers.guards import text_convert_gurad
from const.text import ERRORS

class AnimalIndex:
    def __init__(self, classifier) -> None:
        self.data: list[Animal] = []
        self.temp_data: list[Animal] = []
        self.classifier = classifier

        self.current_id = 0

    def load_file(self, path):
        file = open(path, "r")
        raw_data = file.readlines()
        self.data = [self.convert_data(str_data) for str_data in raw_data]
        self.temp_data = self.data
    
    def generate_id(self):
        id = self.current_id
        self.current_id += 1
        return id

    def convert_data(self, data):
        if ";" in data:
            properties = data.split(";")

            if len(properties) == 4:
                return Animal(properties, self, self.classifier)
            else:
                return ERRORS.ANIMAL_IMPORT
        else:
            return ERRORS.ANIMAL_IMPORT
    
    def clear(self):
        self.temp_data = self.data

    def sort(self, parameter):
        self.temp_data  = sorted(self.temp_data, key=lambda x: getattr(x, parameter[1:]))

    def filter(self, type, value):
        if type == FILTER_TYPES[-1]:
            if value[0] == "-":
                self.temp_data = list(filter(lambda x: getattr(x, type) <= abs(int(value)), self.temp_data))
            else:
                if(text_convert_gurad(value)):
                    self.temp_data = list(filter(lambda x: getattr(x, type) >= int(value), self.temp_data))
                else:
                    print(ERRORS.FILTER_ARG)
        elif type == FILTER_TYPES[-2]:
            self.temp_data = list(filter(lambda x: getattr(x, type) == value, self.temp_data))
        else:
            self.temp_data = list(filter(lambda x: getattr(x, type) == value[1:], self.temp_data))