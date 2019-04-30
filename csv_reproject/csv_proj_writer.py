from typing import TextIO, List


class CsvProjWriter:

    def __init__(
            self,
            file: TextIO,
            to_x_header: str,
            to_y_header: str,
    ):
        self.file = file
        self.to_x_header = to_x_header
        self.to_y_header = to_y_header

    def write_headers(self, headers: List[str]):
        headers.extend([self.to_x_header, self.to_y_header])
        print(headers)

    def write_row(self, row: List[str], x: float, y: float):
        row.extend([str(x), str(y)])
        print(row)
