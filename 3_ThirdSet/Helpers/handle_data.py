import json
import csv
from typing import List, Dict
from datetime import datetime


def calculate_person_age(birth_date: str, death_date: str = None) -> int:
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.strptime(death_date, "%Y-%m-%d") if death_date else datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def list_of_persons(persons: list, name_of_list: str = "") -> None:
    if name_of_list != "":
        print(f"\n{name_of_list} ({len(persons)}):")
    for person in persons:
        death_date = person.get("death_date")
        age = calculate_person_age(person["birth_date"], death_date)
        print(f" {person["name"]} ", end="")
        if death_date:
            print(f"(died on {death_date} at the age of {age})")
        else:
            print(f"({age} year old)")


def load_json_file_content(file_name: str) -> List[Dict[str, str]]:
    with open(file_name, 'r') as json_file:
        return json.load(json_file)


def load_csv_file_content(file_name: str, separator: str = ","):
    with open(file_name, 'r') as csv_file:
        rows = csv.DictReader(csv_file, delimiter=separator)
        return [row for row in rows]
