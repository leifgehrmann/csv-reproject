from typing import List


class CsvProjRow:

    def __init__(self, row: List[str], x: float, y: float):
        self.row = row
        self.x = x
        self.y = y
