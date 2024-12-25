# base_model.py
from datetime import date
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from D_Set.Helpers.ORM.sqlite_client import SQLiteClient
import os

os.makedirs('data', exist_ok=True)

class Model(ABC):
    data: Dict[str, Any] = {}
    created_at: str = None
    sqlite_client: SQLiteClient = None

    def __init__(self, initial_data: Optional[Dict[str, Any]] = None):
        self.sqlite_client = SQLiteClient('data/db.sqlite3')
        self.create_table()
        if initial_data:
            if ((self.created_at is not None) and (initial_data.get(self.created_at) is None)):
                initial_data[self.created_at] = date.today().isoformat()

            if initial_data.get("id"):
                self.update_table_data(initial_data)
            else:
                self.insert_data(initial_data)

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    @property
    @abstractmethod
    def structure(self) -> Dict[str, Any]:
        pass

    def create_table(self) -> None:
        columns = ', '.join(f"{key} {self._get_sqlite_type(value)}" for key, value in self.structure.items() if key != "id")
        self.sqlite_client.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, {columns})")
        self.sqlite_client.connection.commit()

    def _get_sqlite_type(self, py_type: type) -> str:
        if py_type == int:
            return "INTEGER"
        elif py_type == str:
            return "TEXT"
        elif py_type == float:
            return "REAL"
        else:
            return "BLOB"

    def update_table_schema(self) -> None:
        existing_columns = self.get_existing_columns()
        for column, column_type in self.structure.items():
            if column not in existing_columns:
                self.sqlite_client.cursor.execute(f"ALTER TABLE {self.table_name} ADD COLUMN {column} {self._get_sqlite_type(column_type)}")
        self.sqlite_client.connection.commit()

    def get_existing_columns(self) -> List[str]:
        self.sqlite_client.cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns_info = self.sqlite_client.cursor.fetchall()
        return [column[1] for column in columns_info]

    def update_table_data(self, data: Dict[str, Any]) -> None:
        self.sqlite_client.update(self.table_name, data)
        self.data = data
        print(f"Updated table '{self.table_name}' with data: {data}")

    def find(self, item_id: Any) -> Dict[str, Any]:
        if item_id is None:
            return self.data

        item = self.sqlite_client.get(self.table_name, item_id)
        print(f"Retrieved item from table '{self.table_name}' with ID: {item_id}")
        return item

    def find_all_items(self) -> List[Dict[str, Any]]:
        items = self.sqlite_client.get_all(self.table_name)
        print(f"Retrieved all items from table '{self.table_name}'")
        return items

    def find_filtered_items(self, filter_criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        items = self.sqlite_client.get_filtered(self.table_name, filter_criteria)
        print(f"Retrieved filtered items from table '{self.table_name}' with criteria: {filter_criteria}")
        return items

    def insert_data(self, data: Dict[str, Any]) -> None:
        data["id"] = self.sqlite_client.insert(self.table_name, data)
        self.data = data
        print(f"Inserted data into table '{self.table_name}' with data: {data}")

    def delete_item(self, item_id: Any) -> None:
        self.sqlite_client.delete(self.table_name, item_id)
        self.data = {}
        print(f"Deleted item from table '{self.table_name}' with ID: {item_id}")

    def get(self, key: str) -> Any:
        return self.data.get(key)

    def __str__(self):
        items = self.data.items()
        return f"{items}"