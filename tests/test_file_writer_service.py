import unittest
from services import FileWriterService
from exceptions import InvalidFileHeadersException, InvalidFileDataException, DataFileNotCreatedException


class TestFileWriterService(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFileWriterService, self).__init__(*args, **kwargs)
        self._file_writer_service = FileWriterService()
        self._invalid_headers = []
        self._valid_headers = ["id", "title"]
        self._csv_data = [{"id": 1, "title": "This is a title!"}]
        self._excel_data = [[1, "This is a title!"]]

    def test_create_csv_file_invalid_headers(self):
        with self.assertRaises(InvalidFileHeadersException):
            self._file_writer_service.create_csv_file(self._invalid_headers, self._csv_data)

    def test_create_csv_file_invalid_data(self):
        with self.assertRaises(InvalidFileDataException):
            self._file_writer_service.create_csv_file(self._valid_headers, self._excel_data)

    def test_create_excel_file_invalid_headers(self):
        with self.assertRaises(InvalidFileHeadersException):
            self._file_writer_service.create_excel_file(self._invalid_headers, self._excel_data)

    def test_create_excel_file_invalid_data(self):
        with self.assertRaises(InvalidFileDataException):
            self._file_writer_service.create_excel_file(self._valid_headers, self._csv_data)
