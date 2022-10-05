import os
import datetime
import csv
from openpyxl import Workbook
from exceptions import InvalidFileHeadersException, InvalidFileDataException, DataFileNotCreatedException


class FileWriterService:
    def __init__(self):
        self._root_dir = os.path.dirname(os.path.dirname(__file__))
        self._data_dir = os.path.join(self._root_dir, "data")
        self._file_name = f"news_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}"

        if not os.path.exists(self._data_dir):
            os.mkdir(self._data_dir)

    def create_csv_file(self, headers: [str], data: [dict]):
        try:
            if len(headers) == 0:
                raise InvalidFileHeadersException

            if len(data) == 0:
                raise InvalidFileDataException

            if type(data[0]) is not dict:
                raise InvalidFileDataException

            with open(os.path.join(self._data_dir, self._file_name + '.csv'), "w", encoding="UTF8") as f:
                csv_writer = csv.DictWriter(f, fieldnames=headers)
                csv_writer.writeheader()
                csv_writer.writerows(data)
        except (InvalidFileHeadersException, InvalidFileDataException):
            raise
        except Exception as e:
            raise DataFileNotCreatedException(e)

    def create_excel_file(self, headers: [str], data: []):
        try:
            if len(headers) == 0:
                raise InvalidFileHeadersException

            if len(data) == 0:
                raise InvalidFileDataException

            if type(data[0]) is not list:
                raise InvalidFileDataException

            workbook = Workbook()
            sheet_one = workbook.active
            sheet_one.title = 'News'
            sheet_one.append(headers)

            for news in data:
                sheet_one.append(news)

            workbook.save(filename=os.path.join(self._data_dir, self._file_name) + '.xlsx')
        except (InvalidFileHeadersException, InvalidFileDataException):
            raise
        except Exception as e:
            raise DataFileNotCreatedException(e)
