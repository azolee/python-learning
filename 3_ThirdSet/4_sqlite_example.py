import sqlite3
import os
from typing import List, Dict
from Helpers.handle_data import load_json_file_content, list_of_persons, calculate_person_age

os.makedirs('./data', exist_ok=True)

connection = sqlite3.connect('./data/db.sqlite3')
DB = connection.cursor()

DB.execute('''
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    death_date TEXT
)
''')

csalad: List[Dict[str, str]] = load_json_file_content("./data/random_people.json")

persons = [(person.get("name"), person.get("birth_date"), person.get("death_date")) for person in csalad]

DB.executemany('''
INSERT INTO persons (name, birth_date, death_date)
VALUES (?, ?, ?)
''', persons)
connection.commit()

DB.execute('SELECT * FROM persons WHERE birth_date < "1980-01-01"')
connection.commit()
column_names = [description[0] for description in DB.description]
rows = DB.fetchmany(100)
result_list = [dict(zip(column_names, row)) for row in rows]

list_of_persons(persons=result_list, name_of_list="Result list")

DB.close()