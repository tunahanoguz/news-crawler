class Category:
    def __init__(self, name, feed_links):
        self._name = name
        self._feed_links = feed_links

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def feed_links(self):
        return self._feed_links

    @feed_links.setter
    def feed_links(self, value):
        self._feed_links = value

    def __str__(self):
        return f"Name: {self._name}, Feed Links Length: {len(self._feed_links)}"
