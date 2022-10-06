It's a project that the news articles that published on most well-known english news sites crawled and saved.

## News Categories
- Technology
- Politics
- Economy & Finance
- Science
- Health
- Nature & Environment & Energy
- World News from different regions

## Requirements
- feedparser
- goose3
- nltk
- psycopg2
- openpyxl

```bash
pip install -r requirements.txt
```

## Configuration

There are `configs` folder in root directory of the project. The most **important** configuration file is `database_config.ini` file. You can edit this file to connect to the PostgreSQL database.