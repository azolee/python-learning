# sqlite_client.py
import sqlite3
from typing import Dict, Any, List

class SQLiteClient:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def update(self, table_name: str, data: Dict[str, Any]) -> None:
        columns = ', '.join(f"{key} = ?" for key in data.keys())
        values = list(data.values())
        self.cursor.execute(f"UPDATE {table_name} SET {columns} WHERE id = ?", values + [data['id']])
        self.connection.commit()

    def get(self, table_name: str, item_id: Any) -> Dict[str, Any]:
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (item_id,))
        row = self.cursor.fetchone()
        if row:
            column_names = [description[0] for description in self.cursor.description]
            return dict(zip(column_names, row))
        return {}

    def get_all(self, table_name: str) -> List[Dict[str, Any]]:
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        column_names = [description[0] for description in self.cursor.description]
        return [dict(zip(column_names, row)) for row in rows]

    def get_filtered(self, table_name: str, filter_criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        criteria = ' AND '.join(f"{key} = ?" for key in filter_criteria.keys())
        values = list(filter_criteria.values())
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {criteria}", values)
        rows = self.cursor.fetchall()
        column_names = [description[0] for description in self.cursor.description]
        return [dict(zip(column_names, row)) for row in rows]

    def insert(self, table_name: str, data: Dict[str, Any]) -> int:
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' for _ in data.values())
        values = list(data.values())
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
        self.connection.commit()
        return self.cursor.lastrowid

    def delete(self, table_name: str, item_id: Any) -> None:
        self.cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (item_id,))
        self.connection.commit()