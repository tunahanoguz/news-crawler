class InvalidPublishedDateException(Exception):
    def __init__(self):
        super().__init__("Invalid published date!")
