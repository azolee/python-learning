# writer_strategy.py
from abc import ABC, abstractmethod
from typing import List, Dict

class WriterStrategy(ABC):
    @abstractmethod
    def write(self, file_path: str, data: List[Dict[str, str]]) -> None:
        pass