from typing import Dict, Any, List
from D_Set.Helpers.ORM.base_model import Model
from D_Set.Helpers.ORM.sqlite_client import SQLiteClient


class Student(Model):
    created_at: str = "enrollment_date"
    @property
    def table_name(self) -> str:
        return "students"

    @property
    def structure(self) -> Dict[str, Any]:
        return {
            "id": int,
            "name": str,
            "age": int,
            "email": str,
            "enrollment_date": str
        }

    def get_grades(self) -> List[Dict[str, Any]]:
        query = f"""
        SELECT g.grade, g.grade_date, s.name as subject_name
        FROM grades g
        JOIN subjects s ON g.subject_id = s.id
        WHERE g.student_id = ?
        """
        self.sqlite_client.cursor.execute(query, (self.data["id"],))
        grades = self.sqlite_client.cursor.fetchall()
        return [dict(zip(["grade", "grade_date", "subject_name"], grade)) for grade in grades]

    def get_average_grade(self, subject_id: int, start_date: str, end_date: str) -> float:
        query = f"""
        SELECT AVG(g.grade)
        FROM grades g
        WHERE g.student_id = ? AND g.subject_id = ? AND g.grade_date BETWEEN ? AND ?
        """
        self.sqlite_client.cursor.execute(query, (self.data["id"], subject_id, start_date, end_date))
        average_grade = self.sqlite_client.cursor.fetchone()[0]
        return average_grade if average_grade is not None else 0.0
