# Twitter Symbol Scraper

This project scrapes Twitter profiles for mentions of a specific stock symbol

## Installation

1. Clone the repository to your local machine
  ```bash
   $ git clone `<repository-url>`
  ```

2. Update the `ticker` variable in `twitter.py` with the stock symbol you want to search for (e.g., `$TSLA`).

3. Download the Chrome WebDriver executable from [here](https://chromedriver.chromium.org/downloads) and place it in the project directory.

```bash
   $ pip install selenium beautifulsoup4
```

## Usage

1. Update the `twitter_accounts` list in `twitter.py` with the URLs of the Twitter accounts you want to scrape.

2. Update the `ticker` variable in `twitter.py` with the stock symbol you want to search for (e.g., `$TSLA`).

3. Run the `twitter.py` script:
```bash
   $ python twitter.py
```


5. The script will display the number of times the stock symbol was mentioned

## Configuration

- `twitter_accounts`: List of Twitter account URLs to scrape.
- `ticker`: Ticker symbol to look for.
- `interval`: Time interval for scraping session in minutes.



