class FeedLink:
    def __init__(self, news_company, link):
        self._news_company = news_company
        self._link = link

    @property
    def news_company(self):
        return self._news_company

    @news_company.setter
    def news_company(self, value):
        self._news_company = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    def __str__(self):
        return f"News Company: {self._news_company}, Link: {self._link}"
