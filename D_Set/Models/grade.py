from typing import Dict, Any
from D_Set.Helpers.ORM.base_model import Model


class Grade(Model):
    created_at: str = "grade_date"
    @property
    def table_name(self) -> str:
        return "grades"

    @property
    def structure(self) -> Dict[str, Any]:
        return {
            "id": int,
            "student_id": int,
            "subject_id": int,
            "grade": int,
            "grade_date": str
        }
