import csv
import re
from typing import List, Iterator, TextIO, Optional
from csv_reproject import CsvProjRow


class CsvProjReader:

    def __init__(
            self,
            file: TextIO,
            from_x_column: str,
            from_y_column: str,
            from_x_format: str,
            from_y_format: str
    ):
        """
        :param file:
            The CSV file to read
        :param from_x_column:
            The name of the column to read the X (easting) value from
        :param from_y_column:
            The name of the column to read the y (northing) value from
        :param from_x_format:
            The regex pattern to match from the X column
        :param from_y_format:
            The regex pattern to match from the Y column
        """
        self.file = file
        self.from_x_column = from_x_column
        self.from_y_column = from_y_column
        self.from_x_format = from_x_format
        self.from_y_format = from_y_format

        self.csv_reader = csv.reader(self.file, delimiter=',')
        self.headers = next(self.csv_reader)

        self.from_x_column_index = self._get_x_column_index()
        self.from_y_column_index = self._get_y_column_index()

    def read_headers(self) -> List[str]:
        """
        :return:
            returns the column names in the first row of the CSV
        """
        return self.headers

    def read_proj_rows(self) -> Iterator[CsvProjRow]:
        """
        :return:
            returns the rows of the CSV, with the parsed easting and northing
            of the Coordinate reference system
        """
        for row in self.csv_reader:
            x_column_value = row[self.from_x_column_index]
            y_column_value = row[self.from_y_column_index]
            x = self._read_x_value_from_column_value(x_column_value)
            y = self._read_y_value_from_column_value(y_column_value)
            yield CsvProjRow(row, x, y)

    def _get_x_column_index(self) -> int:
        """
        :return:
            returns the column index for the x column
        """
        return self.headers.index(self.from_x_column)

    def _get_y_column_index(self) -> int:
        """
        :return:
            returns the column index for the y column
        """
        return self.headers.index(self.from_y_column)

    def _read_x_value_from_column_value(
            self,
            column_value: str
    ) -> Optional[float]:
        """
        :param column_value:
            the value from the x column
        :return:
            the x (easting) value
        """
        return self._read_number_from_column_value(
            column_value,
            self.from_x_format
        )

    def _read_y_value_from_column_value(
            self,
            column_value: str
    ) -> Optional[float]:
        """
        :param column_value:
            the value from the y column
        :return:
            the y (northing) value
        """
        return self._read_number_from_column_value(
            column_value,
            self.from_y_format
        )

    @staticmethod
    def _read_number_from_column_value(
            column_value: str,
            pattern: str
    ) -> Optional[float]:
        """
        :param column_value:
            the value from a column
        :return:
            the pattern matched numeric value
        """
        matches = re.search(pattern, column_value)

        if matches and len(matches.groups()) == 1:
            return float(matches.group(1))
        return None
