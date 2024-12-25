from typing import Dict, Any
from D_Set.Helpers.ORM.base_model import Model


class Subject(Model):
    @property
    def table_name(self) -> str:
        return "subjects"

    @property
    def structure(self) -> Dict[str, Any]:
        return {
            "id": int,
            "name": int,
        }
