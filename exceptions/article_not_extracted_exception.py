class ArticleNotExtractedException(Exception):
    def __init__(self):
        super().__init__("Article could not be extracted!")
