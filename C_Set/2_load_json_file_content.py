from Helpers.handle_data import load_json_file_content, calculate_person_age, list_of_persons
from typing import List, Dict


persons: List[Dict[str, str]] = load_json_file_content("./data/random_people.json")

list_of_persons(persons=persons, name_of_list="Every person")

adults = list(filter(lambda person: calculate_person_age(person["birth_date"]) > 18, persons))
list_of_persons(persons=adults, name_of_list="Adults")

kids = list(filter(lambda person: calculate_person_age(person["birth_date"]) <= 18, persons))
list_of_persons(persons=kids, name_of_list="Kids")