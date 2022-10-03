import os
import datetime
import csv
from openpyxl import Workbook


class FileWriterService:
    def __init__(self):
        self._root_dir = os.path.dirname(os.path.dirname(__file__))
        self._file_name = f"news_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}"

    def create_csv_file(self, headers: [str], data: []):
        with open(os.path.join(self._root_dir, self._file_name + '.csv'), "w", encoding="UTF8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(data)

    def create_excel_file(self, headers: [str], data: []):
        workbook = Workbook()
        sheet_one = workbook.active
        sheet_one.title = 'News'
        sheet_one.append(headers)

        for news in data:
            sheet_one.append(news)

        workbook.save(filename=self._file_name + '.xlsx')
