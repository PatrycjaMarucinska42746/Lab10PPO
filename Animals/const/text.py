NAMES = [
    "Burek", "Mruczek", "Kropka", "Luna", "Rex", 
    "Kicia", "Bella", "Max", "Mia", "Rocky",
    "Milo", "Lola", "Charlie", "Daisy", "Leo",
    "Molly", "Shadow", "Oreo", "Coco", "Simba",
    "Lucy", "Chloe", "Zeus", "Lily", "Oliver",
    "Cleo", "Tiger", "Buddy", "Misty", "Mochi",
    "Nala", "Ginger", "Blue", "Duke", "Whiskers",
    "Sasha", "Teddy", "Casper", "Smokey", "Toby",
    "Ruby", "Rosie", "Finn", "Maddie", "Milo",
    "Princess", "Riley", "Lulu", "Zoe", "Kai",
    "Harley", "Mochi", "Jasper", "Coco", "Charlie",
    "Lola", "Ziggy", "Lily", "Penny", "Zara",
    "Maximus", "Sophie", "Rocky", "Bentley", "Misty",
    "Smokey", "Maggie", "Ziggy", "Chloe", "Daisy",
    "Zeus", "Leo", "Nala", "Oscar", "Mia",
    "Tucker", "Rusty", "Bella", "Chester", "Lola",
    "Dexter", "Milo", "Sasha", "Oliver", "Maddie",
    "Simba", "Coco", "Roxy", "Lucy", "Teddy",
    "Whiskers", "Ruby", "Toby", "Daisy", "Max",
    "Lulu", "Lily", "Zoe", "Mochi", "Misty"
]

HELP_TEXT = '''quit                Exit the application
list                Writes out all animals from list
list x              Writes out all x animals from list
count               Writes out number of the animals
sort x              Sort animals array by some x filter (-name, -age, -id, -kind, etc.)
filter:group x      Filter list by group name (-mammal, -reptile, -bird, etc.)
filter:species x    Filter list by species name (-giraffe, -zebra, -lion, etc)
filter:gender x     Filter list by gender (-m, -f)
filter:age x        Filter list by some age
clear               Reset filters and sorts
generate x          Generate x random animals
'''

class ERRORS:
    COMMAND = "Incorrect command, please type 'help' for instruction"
    LIST_LEN = "Incorrect records number"
    SORT_NAME = "Incorrect sort type name"
    FILTER_NAME = "Incorrect filter type name"
    FILTER_ARG = "Incorrect filter arugment"
    GENERATE_ARG = "Incorrect generator argument"
    ANIMAL_IMPORT = "Incorrect data in animals.txt file"

class MODES:
    HELP = "help"
    LIST = "list"
    QUIT = "quit"
    COUNT = "count"
    SORT = "sort"
    FILTER = "filter"
    CLEAR = "clear"
    RANDOM = "random"
    GENERATE= "generate"

SORT_TYPES = ["-name", "-age", "-id"]
FILTER_TYPES = ["group", "species", "gender", "age"]