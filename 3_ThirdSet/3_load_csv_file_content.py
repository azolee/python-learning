from Helpers.handle_data import load_csv_file_content, calculate_person_age, list_of_persons
from typing import List, Dict

# Load the data from the file
persons = load_csv_file_content("./data/random_people_comma.csv")

list_of_persons(persons=persons, name_of_list="Every person")

adults = list(filter(lambda person: calculate_person_age(person["birth_date"]) > 18, persons))
list_of_persons(persons=adults, name_of_list="Adults")

kids = list(filter(lambda person: calculate_person_age(person["birth_date"]) <= 18, persons))
list_of_persons(persons=kids, name_of_list="Kids")

# Load the same data with semicolon separator
persons = load_csv_file_content("./data/random_people_semicolon.csv", ";")

list_of_persons(persons=persons, name_of_list="Every person - data separated with semicolon")

adults = list(filter(lambda person: calculate_person_age(person["birth_date"]) > 18, persons))
list_of_persons(persons=adults, name_of_list="Adults - data separated with semicolon")

kids = list(filter(lambda person: calculate_person_age(person["birth_date"]) <= 18, persons))
list_of_persons(persons=kids, name_of_list="Kids - data separated with semicolon")