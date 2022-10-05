class DataFileNotCreatedException(Exception):
    def __init__(self, msg):
        super().__init__(f"Data file could not be created! {msg}")
