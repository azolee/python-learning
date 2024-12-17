# csv_writer_strategy.py
import csv
from typing import List, Dict
from D_Set.Helpers.Writer.writer_strategy import WriterStrategy


class CSVWriterStrategy(WriterStrategy):
    def write(self, file_path: str, data: List[Dict[str, str]]) -> None:
        if not data:
            return
        fieldnames = set()
        for row in data:
            fieldnames.update(row.keys())
        fieldnames = list(fieldnames)

        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)