class InvalidFileDataException(Exception):
    def __init__(self):
        super().__init__("Invalid data for creating a CSV file!")
