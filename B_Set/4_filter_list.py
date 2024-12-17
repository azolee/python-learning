from typing import List, Dict

persons: List[Dict[str, int]] = [
    { "name": 'John Doe', "age": 45},
    { "name": 'Jane Smith', "age": 44},
    { "name": 'Alice Johnson', "age": 48},
    { "name": 'Bob Brown', "age": 77},
    { "name": 'Carol White', "age": 72},
    { "name": 'David Green', "age": 68},
    { "name": 'Eve Black', "age": 68},
    { "name": 'Frank Blue', "age": 7},
    { "name": 'Grace Red', "age": 10},
    { "name": 'Hank Yellow', "age": 5},
    { "name": 'Ivy Purple', "age": 2},
]

def list_of_persons(persons: list, name_of_list: str = "") -> None:
    if name_of_list != "":
        print(f"\n{name_of_list}:")
    for person in persons:
        print(f'{person["name"]} ({person["age"]}yo)')

list_of_persons(persons=persons, name_of_list="All persons")

grandparents = list(filter(lambda person: person['age'] > 65, persons))
list_of_persons(persons=grandparents, name_of_list="Grandparents")

parents = list(filter(lambda person: 65 >= person['age'] > 18, persons))
list_of_persons(persons=parents, name_of_list="Parents")

adults = list(filter(lambda person: person['age'] > 18, persons))
list_of_persons(persons=adults, name_of_list="Adults")

kids = list(filter(lambda person: person['age'] <= 18, persons))
list_of_persons(persons=kids, name_of_list="Kids")
