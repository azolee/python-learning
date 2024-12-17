# writer.py
from typing import List, Dict

from D_Set.Helpers.Writer.json_writer_strategy import JSONWriterStrategy
from D_Set.Helpers.Writer.writer_strategy import WriterStrategy


class Writer:
    strategy: WriterStrategy

    def __init__(self, strategy: WriterStrategy = None):
        self.set_strategy(strategy)


    def set_strategy(self, strategy: WriterStrategy = None) -> None:
        self.strategy = strategy or JSONWriterStrategy()


    def write(self, file_path: str, data: List[Dict[str, str]]) -> None:
        self.strategy.write(file_path, data)