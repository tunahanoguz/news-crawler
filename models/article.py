class Article:
    def __init__(self, title, description, content, tags, link, category, company, published_date, article_id=0):
        self._id = article_id
        self._title = title
        self._description = description
        self._content = content
        self._tags = tags
        self._link = link
        self._category = category
        self._company = company
        self._published_date = published_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

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

    @property
    def published_date(self):
        return self._published_date

    @published_date.setter
    def published_date(self, value):
        self._published_date = value

    def __str__(self):
        return f"ID: {self._id if self._id is not None else 0}, " \
               f"Title: {self._title}, Content: {self._content}, " \
               f"Link: {self._link}, Category: {self._category}, " \
               f"Company: {self._company}, Published Date: {self._published_date}"
