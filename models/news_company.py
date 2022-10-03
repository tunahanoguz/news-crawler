class NewsCompany:
    def __init__(self, name, alias):
        self._name = name
        self._alias = alias

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    def __str__(self):
        return f"Name: {self._name}, Link: {self._alias}"
