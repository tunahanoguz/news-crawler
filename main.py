from models import NewsCompany, Category, FeedLink
from services import CrawlerService, ArticleService, FileWriterService

news_companies = [
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


def get_news_company(link):
    return list(filter(lambda company: company.alias in link, news_companies))[0].name


categories = [
    Category(
        "Technology",
        [FeedLink(get_news_company(link), link)
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
        [FeedLink(get_news_company(link), link)
         for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000113",
                      "https://moxie.foxnews.com/google-publisher/politics.xml",
                      "http://feeds.skynews.com/feeds/rss/politics.xml",
                      "https://www.reutersagency.com/feed/?best-topics=political-general&post_type=best",
                      "https://www.express.co.uk/posts/rss/139/politics"]]
    ),
    Category(
        "World News",
        [FeedLink(get_news_company(link), link)
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
        [FeedLink(get_news_company(link), link)
         for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15837362",
                      "https://moxie.foxnews.com/google-publisher/us.xml",
                      "http://feeds.skynews.com/feeds/rss/us.xml",
                      "http://rss.cnn.com/rss/edition_us.rss"]]
    ),
    Category(
        "UK News",
        [FeedLink(get_news_company(link), link)
         for link in ["http://feeds.skynews.com/feeds/rss/uk.xml",
                      "https://www.express.co.uk/posts/rss/1/uk",
                      "https://www.theguardian.com/uk-news/rss"]]
    ),
    Category(
        "Asia News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19832390",
                      "https://www.france24.com/en/asia-pacific/rss",
                      "http://rss.cnn.com/rss/edition_asia.rss",
                      "https://www.reutersagency.com/feed/?best-regions=asia&post_type=best"]]
    ),
    Category(
        "Europe News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19794221",
                      "https://www.france24.com/en/europe/rss",
                      "http://rss.cnn.com/rss/edition_europe.rss",
                      "https://www.reutersagency.com/feed/?best-regions=europe&post_type=best",
                      "https://euronews.com/rss?format=mrss&level=vertical&name=my-europe"]]
    ),
    Category(
        "Middle East News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://www.france24.com/en/middle-east/rss",
                      "http://rss.cnn.com/rss/edition_meast.rss",
                      "https://www.reutersagency.com/feed/?best-regions=middle-east&post_type=best"]]
    ),
    Category(
        "Africa News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://www.france24.com/en/africa/rss",
                      "http://rss.cnn.com/rss/edition_africa.rss",
                      "https://www.reutersagency.com/feed/?best-regions=africa&post_type=best"]]
    ),
    Category(
        "Americas News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://www.france24.com/en/americas/rss",
                      "http://rss.cnn.com/rss/edition_americas.rss",
                      "https://www.reutersagency.com/feed/?best-regions=north-america&post_type=best",
                      "https://www.reutersagency.com/feed/?best-regions=south-america&post_type=best"]]
    ),
    Category(
        "Science News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://moxie.foxnews.com/google-publisher/science.xml",
                      "http://rss.cnn.com/rss/edition_space.rss",
                      "https://www.express.co.uk/posts/rss/151/science",
                      "https://www.theguardian.com/science/rss"]]
    ),
    Category(
        "Economy & Finance News",
        [FeedLink(get_news_company(link), link)
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
        [FeedLink(get_news_company(link), link)
         for link in ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000108",
                      "https://moxie.foxnews.com/google-publisher/health.xml",
                      "https://www.france24.com/en/health/rss",
                      "https://www.reutersagency.com/feed/?best-topics=health&post_type=best",
                      "https://www.express.co.uk/posts/rss/11/health",
                      "https://www.theguardian.com/lifeandstyle/health-and-wellbeing/rss"]]
    ),
    Category(
        "Nature & Environment & Energy News",
        [FeedLink(get_news_company(link), link)
         for link in ["https://www.reutersagency.com/feed/?best-sectors=commodities-energy&post_type=best",
                      "https://www.reutersagency.com/feed/?best-topics=environment&post_type=best",
                      "https://www.express.co.uk/posts/rss/128/nature",
                      "https://euronews.com/rss?format=mrss&level=vertical&name=green",
                      "https://www.theguardian.com/environment/climate-crisis/rss",
                      "https://www.theguardian.com/environment/rss"]]
    )
]


def get_news_and_insert_to_db():
    crawler_service = CrawlerService()
    news_links = crawler_service.get_news_links(categories)

    article_service = ArticleService()

    for news_link in news_links:
        try:
            article = crawler_service.get_news_article(news_link, crawler_service.extract_news_article(news_link))
            article_service.create(article)
        except Exception as e:
            print(e)


def get_all_news_with_header_and_data():
    article_service = ArticleService()
    news_articles = article_service.get_all()

    headers = [list(article.__dict__.keys()) for article in news_articles][0]
    excel_data = [list(article.__dict__.values()) for article in news_articles]
    csv_data = [{header: article.__getattribute__(header) for header in headers} for article in news_articles]
    print(csv_data)

    return {'headers': headers, 'excel_data': excel_data, 'csv_data': csv_data}


def create_excel_file_for_all_news(headers: [str], data: []):
    file_writer_service = FileWriterService()
    file_writer_service.create_excel_file(headers, data)


def create_csv_file_for_all_news(headers: [str], data: []):
    file_writer_service = FileWriterService()
    file_writer_service.create_csv_file(headers, data)


# get_news_and_insert_to_db()
headers_and_data = get_all_news_with_header_and_data()
create_excel_file_for_all_news(headers_and_data['headers'], headers_and_data['excel_data'])
create_csv_file_for_all_news(headers_and_data['headers'], headers_and_data['csv_data'])
