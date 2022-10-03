class ErrorLog:
    def __init__(self, message, occurrence_date):
        self._message = message
        self._occurrence_date = occurrence_date

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def occurrence_date(self):
        return self._occurrence_date

    @occurrence_date.setter
    def occurrence_date(self, value):
        self._occurrence_date = value

    def __str__(self):
        return f"Message: {self._message}, Occurrence Date: {self._occurrence_date}"
