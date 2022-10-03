class InvalidConfigFileException(Exception):
    def __init__(self, msg):
        super().__init__(f"Config file is invalid! {msg}")
