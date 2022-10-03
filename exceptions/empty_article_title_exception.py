class EmptyArticleTitleException(Exception):
    def __init__(self):
        super().__init__("Article title is empty!")
