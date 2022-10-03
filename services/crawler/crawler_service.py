import datetime
import os
import re
import feedparser
from goose3 import Goose, Article as GooseArticle
from models import NewsLink, Article, Category
from exceptions import ArticleNotExtractedException, EmptyArticleContentException, EmptyArticleTitleException, \
    InvalidPublishedDateException

import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords


class CrawlerService:

    @staticmethod
    def get_news_links(categories: [Category]):
        return [
            NewsLink(link=news_link.link, category=category.name, company=feed_link.news_company)
            for category in categories
            for feed_link in category.feed_links
            for news_link in feedparser.parse(feed_link.link).entries
        ]

    @staticmethod
    def extract_news_article(news_link: NewsLink):
        try:
            with Goose() as g:
                return g.extract(url=news_link.link)
        except Exception:
            raise ArticleNotExtractedException

    def get_news_article(self, news_link: NewsLink, extracted_article: GooseArticle):
        try:
            if extracted_article is None:
                raise ArticleNotExtractedException

            if extracted_article.title is None or not extracted_article.title:
                raise EmptyArticleTitleException

            if extracted_article.cleaned_text is None or not extracted_article.cleaned_text:
                raise EmptyArticleContentException

            return Article(title=self._parse_news_txt(extracted_article.title),
                           description=self._parse_news_txt(extracted_article.meta_description),
                           content=self._parse_news_txt(extracted_article.cleaned_text),
                           tags=extracted_article.tags,
                           link=news_link.link,
                           category=news_link.category,
                           company=news_link.company,
                           published_date=self._parse_published_date(extracted_article.publish_datetime_utc))
        except (EmptyArticleTitleException, EmptyArticleContentException, InvalidPublishedDateException):
            raise
        except Exception:
            raise ArticleNotExtractedException

    @staticmethod
    def _parse_published_date(date):
        try:
            default_date = datetime.datetime.now()
            date = date if date is not None else default_date
            if type(date) is not type(default_date):
                raise InvalidPublishedDateException
            return date
        except Exception:
            raise InvalidPublishedDateException

    @staticmethod
    def _remove_punctuations_from_txt(text: str):
        return re.sub(r'[^\w\s]', ' ', text)

    @staticmethod
    def _remove_one_length_words_from_txt(text: str):
        return ' '.join([word for word in text.split() if len(word) > 1])

    @staticmethod
    def _remove_stop_words_from_txt(text: str):
        return ' '.join([word
                         for word in text.split()
                         if word.lower() not in stopwords.words('english')])

    @staticmethod
    def _remove_most_common_thousand_words_from_txt(text: str):
        with open(os.path.join(os.path.dirname(__file__), 'most_common_thousand_words.txt'), 'r') as f:
            common_words = f.readlines()
            common_words.extend([f"{word}s" for word in common_words])
            common_words.extend([f"{word}d" for word in common_words])
            common_words.extend([f"{word}ed" for word in common_words])
            return ' '.join([word for word in text.split() if word.lower() not in common_words])

    def _parse_news_txt(self, text: str):
        return self._remove_most_common_thousand_words_from_txt(
            self._remove_stop_words_from_txt(
                self._remove_one_length_words_from_txt(
                    self._remove_punctuations_from_txt(text)
                )
            )
        ).split()
