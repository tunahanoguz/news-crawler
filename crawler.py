import logging
from logging.handlers import RotatingFileHandler
from configs import ConfigFileParser
from models import NewsCompany, Category, FeedLink
from services import CrawlerService, ArticleService, ParsedArticleService, FileWriterService


class Crawler:
    def __init__(self):
        self._config_parser = ConfigFileParser('logging_config.ini', 'logging')
        self._logging_config = self._config_parser.parse()

        self._logging = logging.getLogger(__name__)
        self._logging.setLevel(logging.INFO)
        self._logging_handler = RotatingFileHandler(filename=self._logging_config['file_name'],
                                                    maxBytes=int(self._logging_config['max_bytes']),
                                                    backupCount=int(self._logging_config['backup_count']))
        self._logging_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        self._logging_handler.setFormatter(self._logging_formatter)
        self._logging.addHandler(self._logging_handler)

        self._crawler_service = CrawlerService()
        self._article_service = ArticleService()
        self._parsed_article_service = ParsedArticleService()
        self._file_writer_service = FileWriterService()

        self._create_categories()
        self._crawl_news_and_insert_to_db()
        self._get_news_columns_and_data_to_create_data_file()
        
    def _news_company(self, link):
        return list(filter(lambda company: company.alias in link, self._news_companies))[0].name

    def _create_categories(self):
        self._news_companies = [
            NewsCompany("Reuters Agency", "reutersagency"),
            NewsCompany("CNN", "cnn"),
            NewsCompany("Fox News", "foxnews"),
            NewsCompany("CNBC", "cnbc"),
            NewsCompany("The Guardian", "theguardian"),
            NewsCompany("Euronews", "euronews"),
            NewsCompany("France 24", "france24"),
            NewsCompany("Sky News", "skynews"),
            NewsCompany("Express News", "express")
        ]
        
        self._categories = [
            Category(
                "Technology",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910",
                              "https://moxie.foxnews.com/google-publisher/tech.xml",
                              "http://feeds.skynews.com/feeds/rss/technology.xml",
                              "http://rss.cnn.com/rss/edition_technology.rss",
                              "https://www.reutersagency.com/feed/?best-topics=tech&post_type=best",
                              "https://www.express.co.uk/posts/rss/59/tech",
                              "https://www.theguardian.com/uk/technology/rss"]]
            ),
            Category(
                "Politics",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000113",
                              "https://moxie.foxnews.com/google-publisher/politics.xml",
                              "http://feeds.skynews.com/feeds/rss/politics.xml",
                              "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best",
                              "https://www.express.co.uk/posts/rss/139/politics"]]
            ),
            Category(
                "World News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100727362",
                              "https://moxie.foxnews.com/google-publisher/world.xml",
                              "http://feeds.skynews.com/feeds/rss/world.xml",
                              "https://www.france24.com/en/rss",
                              "http://rss.cnn.com/rss/edition_world.rss",
                              "https://www.reutersagency.com/feed/?taxonomy=best-regions&post_type=best",
                              "https://www.express.co.uk/posts/rss/78/world",
                              "https://www.euronews.com/rss?format=mrss&level=theme&name=news",
                              "https://www.theguardian.com/world/rss"]]
            ),
            Category(
                "US News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15837362",
                              "https://moxie.foxnews.com/google-publisher/us.xml",
                              "http://feeds.skynews.com/feeds/rss/us.xml",
                              "http://rss.cnn.com/rss/edition_us.rss"]]
            ),
            Category(
                "UK News",
                [FeedLink(self._news_company(link), link)
                 for link in ["http://feeds.skynews.com/feeds/rss/uk.xml",
                              "https://www.express.co.uk/posts/rss/1/uk",
                              "https://www.theguardian.com/uk-news/rss"]]
            ),
            Category(
                "Asia News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19832390",
                              "https://www.france24.com/en/asia-pacific/rss",
                              "http://rss.cnn.com/rss/edition_asia.rss",
                              "https://www.reutersagency.com/feed/?best-regions=asia&post_type=best"]]
            ),
            Category(
                "Europe News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19794221",
                              "https://www.france24.com/en/europe/rss",
                              "http://rss.cnn.com/rss/edition_europe.rss",
                              "https://www.reutersagency.com/feed/?best-regions=europe&post_type=best",
                              "https://euronews.com/rss?format=mrss&level=vertical&name=my-europe"]]
            ),
            Category(
                "Middle East News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://www.france24.com/en/middle-east/rss",
                              "http://rss.cnn.com/rss/edition_meast.rss",
                              "https://www.reutersagency.com/feed/?best-regions=middle-east&post_type=best"]]
            ),
            Category(
                "Africa News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://www.france24.com/en/africa/rss",
                              "http://rss.cnn.com/rss/edition_africa.rss",
                              "https://www.reutersagency.com/feed/?best-regions=africa&post_type=best"]]
            ),
            Category(
                "Americas News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://www.france24.com/en/americas/rss",
                              "http://rss.cnn.com/rss/edition_americas.rss",
                              "https://www.reutersagency.com/feed/?best-regions=north-america&post_type=best",
                              "https://www.reutersagency.com/feed/?best-regions=south-america&post_type=best"]]
            ),
            Category(
                "Science News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://moxie.foxnews.com/google-publisher/science.xml",
                              "http://rss.cnn.com/rss/edition_space.rss",
                              "https://www.express.co.uk/posts/rss/151/science",
                              "https://www.theguardian.com/science/rss"]]
            ),
            Category(
                "Economy & Finance News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=20910258",
                              "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664",
                              "http://rss.cnn.com/rss/money_news_international.rss",
                              "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
                              "https://www.express.co.uk/posts/rss/21/finance",
                              "https://www.theguardian.com/uk/money/rss",
                              "https://www.theguardian.com/uk/business/rss"]]
            ),
            Category(
                "Health News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000108",
                              "https://moxie.foxnews.com/google-publisher/health.xml",
                              "https://www.france24.com/en/health/rss",
                              "https://www.reutersagency.com/feed/?best-topics=health&post_type=best",
                              "https://www.express.co.uk/posts/rss/11/health",
                              "https://www.theguardian.com/lifeandstyle/health-and-wellbeing/rss"]]
            ),
            Category(
                "Nature & Environment & Energy News",
                [FeedLink(self._news_company(link), link)
                 for link in ["https://www.reutersagency.com/feed/?best-sectors=commodities-energy&post_type=best",
                              "https://www.reutersagency.com/feed/?best-topics=environment&post_type=best",
                              "https://www.express.co.uk/posts/rss/128/nature",
                              "https://euronews.com/rss?format=mrss&level=vertical&name=green",
                              "https://www.theguardian.com/environment/climate-crisis/rss",
                              "https://www.theguardian.com/environment/rss"]]
            )
        ]

    def _crawl_news_and_insert_to_db(self):
        news_links = self._crawler_service.get_news_links(self._categories)

        for news_link in news_links:
            try:
                article = self._crawler_service.get_news_article(
                    news_link,
                    self._crawler_service.extract_news_article(news_link)
                )
                self._article_service.create(article)

                parsed_article = self._crawler_service.parse_news_article(article)
                self._parsed_article_service.create(parsed_article)

            except Exception as e:
                logging.exception(e)

    def _get_news_columns_and_data_to_create_data_file(self):
        news_articles = self._article_service.get_all()

        self._file_headers = [list(article.__dict__.keys()) for article in news_articles][0]
        self._excel_data = [list(article.__dict__.values()) for article in news_articles]
        self._csv_data = [{header: article.__getattribute__(header) for header in self._file_headers}
                          for article in news_articles]

    def create_excel_file_for_all_news(self):
        self._file_writer_service.create_excel_file(self._file_headers, self._excel_data)

    def create_csv_file_for_all_news(self):
        self._file_writer_service.create_csv_file(self._file_headers, self._csv_data)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.create_excel_file_for_all_news()
    crawler.create_csv_file_for_all_news()
