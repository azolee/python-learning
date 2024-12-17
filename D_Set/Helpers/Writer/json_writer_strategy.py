# json_writer_strategy.py
import json
import os
from typing import List, Dict
from D_Set.Helpers.Writer.writer_strategy import WriterStrategy


class JSONWriterStrategy(WriterStrategy):
    def write(self, file_path: str, data: List[Dict[str, str]]) -> None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)