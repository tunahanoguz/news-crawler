class DbConnectionException(Exception):
    def __init__(self):
        super().__init__('There is an db connection error! Please check your connection arguments.')
