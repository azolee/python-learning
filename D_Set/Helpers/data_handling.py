from os.path import split
from typing import List, Dict, Callable, Any
from tqdm import tqdm

from C_Set.Helpers.handle_data import calculate_person_age, load_json_file_content, load_csv_file_content
from faker import Faker
import random


def print_person(person) -> str:
    death_date = person.get("death_date")
    age = calculate_person_age(person["birth_date"], death_date)
    info = f"{age} year old"
    if death_date:
        info = f"died on {death_date} at the age of {age}"
    return f" {person['name']}, {person['job']} (Birth date: {person['birth_date']}, {info})"


def print_list_of_persons(persons: list, name_of_list: str = "", formater_function: Callable[[Dict[str, Any]], str] = print_person) -> None:
    if name_of_list != "":
        print(f"\n{name_of_list} ({len(persons)}):")
    for person in persons:
        death_date = person.get("death_date")
        age = calculate_person_age(person["birth_date"], death_date)
        if formater_function:
            print(formater_function(person))
        else:
            print(f" {person['name']} / {person['job']} / ", end="")
            if death_date:
                print(f"died on {death_date} at the age of {age}")
            else:
                print(f"{age} year old")


def generate_fake_persons_data(limit: int = 100) -> List[Dict[str, str]]:
    fake = Faker()
    for i in tqdm(range(1, limit+1), desc="Generating fake persons data"):
        person = {
            "name": fake.name(),
            "job": fake.job(),
            "birth_date": fake.date_of_birth(minimum_age=1, maximum_age=90).strftime("%Y-%m-%d")
        }
        death_date = fake.date_of_birth(minimum_age=0, maximum_age=90).strftime("%Y-%m-%d")
        if random.choice([True, False]) and calculate_person_age(person["birth_date"], death_date) > 60:
            person["death_date"] = death_date
        yield person

from collections import Counter
from typing import List, Dict, Any
from C_Set.Helpers.handle_data import calculate_person_age

def calculate_statistics(persons: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_age = 0
    age_count = 0
    name_counter = Counter()
    job_counter = Counter()
    initials_counter = Counter()

    for person in persons:
        death_date = person.get("death_date")
        age = calculate_person_age(person["birth_date"], death_date)
        total_age += age
        age_count += 1
        name_counter[person["name"]] += 1
        job_counter[person["job"]] += 1
        name = get_name_details(person["name"])
        initials_counter[name['initials']] += 1

    average_age = total_age / age_count if age_count else 0
    most_common_names = name_counter.most_common(5)
    most_common_jobs = job_counter.most_common(5)
    most_common_initials = initials_counter.most_common(5)

    return {
        "total_persons": len(persons),
        "average_age": average_age,
        "most_common_names": most_common_names,
        "most_common_jobs": most_common_jobs,
        "most_common_initials": most_common_initials
    }


def get_name_details(name: str) -> dict[str, str]:
    splitted_name = name.split(" ")
    title = ""
    if (splitted_name[0] in ["Mr.", "Mrs.", "Ms.", "Miss", "Dr."]):
        title = splitted_name[0]
        splitted_name = splitted_name[1:]

    first_name = splitted_name[0]
    last_name = " ".join(splitted_name[1:])
    initials = f"{first_name[0]}{last_name[0]}"

    return {
        "title": title,
        "first_name": first_name,
        "last_name": last_name,
        "initials": initials
    }