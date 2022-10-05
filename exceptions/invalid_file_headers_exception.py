class InvalidFileHeadersException(Exception):
    def __init__(self):
        super().__init__("Invalid headers for creating a CSV file!")
