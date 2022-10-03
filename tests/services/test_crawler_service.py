import datetime
import os
import unittest

from goose3 import Article as GooseArticle

from exceptions import ArticleNotExtractedException, EmptyArticleTitleException, EmptyArticleContentException,\
    InvalidPublishedDateException
from models import NewsLink
from services.crawler import CrawlerService


class TestCrawlerService(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCrawlerService, self).__init__(*args, **kwargs)
        self._news_link = NewsLink(link="https://test-news.test", category="Test Category", company="Test Company")
        self._crawler_service = CrawlerService()

    def test_remove_punctuations_from_txt(self):
        value = self._crawler_service._remove_punctuations_from_txt("You've done the project!")
        self.assertEqual(value, "You ve done the project ")

    def test_remove_one_length_words_from_txt(self):
        value = self._crawler_service._remove_one_length_words_from_txt("This is a news crawler project!")
        self.assertEqual(value, "This is news crawler project!")

    def test_remove_stop_words_from_txt(self):
        self.assertEqual(self._crawler_service._remove_stop_words_from_txt("You are you"), "")

    def test_remove_most_common_thousand_words_from_txt(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        with open(os.path.join(root_dir, 'services/crawler/most_common_thousand_words.txt'), 'r') as f:
            common_words = f.readlines()
        value = self._crawler_service._remove_stop_words_from_txt(f"{common_words[0]}, {common_words[1]}")
        self.assertEqual(value, ",")

    def test_extract_news_article(self):
        with self.assertRaises(ArticleNotExtractedException):
            self._crawler_service.extract_news_article(self._news_link)

    def test_get_news_article_empty_title(self):
        with self.assertRaises(EmptyArticleTitleException):
            article = GooseArticle()
            article._cleaned_text = "Test content."
            article._publish_datetime_utc = datetime.datetime.now().isoformat()
            self._crawler_service.get_news_article(self._news_link, article)

    def test_get_news_article_empty_content(self):
        with self.assertRaises(EmptyArticleContentException):
            article = GooseArticle()
            article._title = "Test Title!"
            article._publish_datetime_utc = datetime.datetime.now().isoformat()
            self._crawler_service.get_news_article(self._news_link, article)

    def test_get_news_article_invalid_published_date(self):
        with self.assertRaises(InvalidPublishedDateException):
            article = GooseArticle()
            article._title = "Test Title!"
            article._cleaned_text = "Test content."
            article._publish_datetime_utc = 123
            self._crawler_service.get_news_article(self._news_link, article)


if __name__ == '__main__':
    unittest.main()
