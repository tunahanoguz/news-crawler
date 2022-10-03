class EmptyArticleContentException(Exception):
    def __init__(self):
        super().__init__("Article content is empty!")
