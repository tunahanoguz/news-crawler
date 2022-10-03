from context_managers import DbContextManager
from models import Category, Article


class ArticleService:
    def __init__(self):
        self.create_table()

    @staticmethod
    def create_table():
        with DbContextManager() as db:
            query = """
                CREATE TABLE IF NOT EXISTS articles (
                    id SERIAL PRIMARY KEY,
                    title TEXT[] NOT NULL,
                    description TEXT[] NOT NULL,
                    content TEXT[] NOT NULL,
                    tags TEXT[],
                    link VARCHAR(255) NOT NULL,
                    category VARCHAR(255) NOT NULL,
                    company VARCHAR(255) NOT NULL,
                    published_date DATE NOT NULL,
                    created_date DATE NOT NULL DEFAULT CURRENT_DATE
                )
            """
            cur = db.cursor()
            cur.execute(query)
            cur.close()

    @staticmethod
    def get_all():
        with DbContextManager() as db:
            query = """
                SELECT  id, title, description,
                        content, tags, link,
                        category, company, published_date, created_date
                FROM articles
            """
            cur = db.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            articles = [Article(row[1], row[2], row[3], row[4], row[5],
                                Category(row[6], row[7]), row[8], row[0])
                        for row in rows]
            cur.close()
            return articles

    @staticmethod
    def get_single(article_id: int):
        with DbContextManager() as db:
            query = """
                SELECT  id, title, description,
                        content, tags, link,
                        category, company, published_date, created_date
                FROM articles
            """
            cur = db.cursor()
            cur.execute(query, (article_id,))
            row = cur.fetchone()
            article = Article(row[1], row[2], row[0], row[3], row[4], Category(row[5], row[6]), row[7], row[8])
            cur.close()
            return article

    @staticmethod
    def create(article: Article):
        with DbContextManager() as db:
            query = """
                INSERT INTO articles (title, description, content, tags, link, category, company, published_date)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;
            """
            cur = db.cursor()
            cur.execute(query, (article.title, article.description, article.content, article.tags,
                                article.link, article.category, article.company, article.published_date))
            article_id = cur.fetchone()[0]
            cur.close()
            return article_id

    @staticmethod
    def update(article: Article):
        with DbContextManager() as db:
            query = """
                UPDATE articles
                SET title = %s,
                    description = %s,
                    content = %s,
                    tags = %s,
                    link = %s,
                    category = %s,
                    company = %s,
                    published_date = %s
                WHERE id = %s
            """
            cur = db.cursor()
            cur.execute(query, (article.title, article.description, article.content, article.tags, article.link,
                                article.category, article.company, article.published_date, article.id))
            updated_rows_count = cur.rowcount
            cur.close()
            return updated_rows_count

    @staticmethod
    def delete(article_id: int):
        with DbContextManager() as db:
            query = """DELETE FROM articles WHERE id = %s"""
            cur = db.cursor()
            cur.execute(query, (article_id,))
            deleted_rows = cur.rowcount
            cur.close()
            return deleted_rows

    @staticmethod
    def delete_all():
        with DbContextManager() as db:
            query = """TRUNCATE TABLE articles"""
            cur = db.cursor()
            cur.execute(query)
            cur.close()
