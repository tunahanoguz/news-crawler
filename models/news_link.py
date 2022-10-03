class NewsLink:
    def __init__(self, link, category, company):
        self._link = link
        self._category = category
        self._company = company

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    def __str__(self):
        return f"Link: {self._link}, Category: {self._category}, Company: {self._company}"
