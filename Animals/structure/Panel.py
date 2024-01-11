from const.text import HELP_TEXT, ERRORS, MODES, SORT_TYPES, FILTER_TYPES
from helpers.guards import text_convert_gurad, split_guard
import random

class Panel:
    def __init__(self, animal_index, animal_generator) -> None:
        self.animal_index = animal_index
        self.animal_generator = animal_generator

    def list(self, len=-1):
        data = self.animal_index.temp_data if len == -1 else self.animal_index.temp_data[:len]

        for animal in data:
            print(animal.str_data())

    def help(self):
        print(HELP_TEXT)

    def count(self):
        print(f'Count: {len(self.animal_index.temp_data)}')
    
    def random(self):
        animal = self.animal_index.temp_data[random.randint(0, len(self.animal_index.temp_data)-1)]
        print(animal.str_data())

    def run(self):
        while True:
            user_action = input("Command: ").lower()

            if user_action == MODES.QUIT:
                return False
            else:
                self.logic(user_action)

    def logic(self, user_action):
        if user_action == MODES.HELP:
            self.help()
        elif user_action == MODES.LIST:
            self.list()
        elif user_action == MODES.COUNT:
            self.count()
        elif user_action == MODES.CLEAR:
            self.animal_index.clear()
        elif user_action == MODES.RANDOM:
                self.random()
        else:
            if "--" in user_action:
                operations = user_action.split("--")[1:]

                for operation in operations:
                    if operation != "" or operation != " ":
                        if operation[-1] == " ":
                            operation = operation[:-1]
                    
                        self.logic(operation)
            elif MODES.LIST in user_action:
                if(text_convert_gurad(user_action[5:])):
                    data_len = int(user_action[5:])

                    if data_len <= len(self.animal_index.temp_data) and data_len > 0:
                        self.list(data_len)
                    else:
                        print(ERRORS.LIST_LEN)
                else:
                    print(ERRORS.LIST_LEN)
            elif MODES.GENERATE in user_action:
                if(text_convert_gurad(user_action[8:])):
                    data_len = int(user_action[8:])

                    if data_len > 0:
                        self.animal_generator.generate(data_len)
                    else:
                        print(ERRORS.GENERATE_ARG)
                else:
                    print(ERRORS.GENERATE_ARG)

            elif MODES.SORT in user_action:
                sort_type = user_action[5:]

                if sort_type in SORT_TYPES:
                    self.animal_index.sort(sort_type)
                else:
                    print(ERRORS.SORT_NAME)
            elif MODES.FILTER in user_action:
                filter_type = user_action[7:]

                if(split_guard(filter_type, " ")):
                    filter_name, filter_value = filter_type.split(" ")

                    if filter_name in FILTER_TYPES:
                        self.animal_index.filter(filter_name, filter_value)
                    else:
                        print(ERRORS.FILTER_NAME)
                else:
                    print(ERRORS.FILTER_NAME)
            else:
                print(ERRORS.COMMAND)