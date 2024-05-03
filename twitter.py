from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_twitter_accounts(twitter_accounts, ticker, interval):
    

    # Set the path to the Chrome driver executable
    chromedriver_path = "chromedriver.exe"
    service = Service(executable_path=chromedriver_path)
    
    # Initialize a Chrome webdriver instance
    driver = webdriver.Chrome(service=service)
    
    symbol_count = 0
    
    # Iterate through each Twitter account
    for account in twitter_accounts:
        # Navigate to the Twitter profile
        driver.get(account)
        
        # Wait for the page to load 
        time.sleep(5)
        
        # Extract the page source
        page_source = driver.page_source
        
        # Create a BeautifulSoup object
        soup = BeautifulSoup(page_source, "html.parser")
        
        # Find all <a> tags containing symbols
        symbol_elements = soup.find_all(lambda tag: tag.name == "a" and tag.string and tag.string.startswith("$"))
        
        # Extract the text of each symbol element and increase counter when find the symbol
        for symbol_element in symbol_elements:
            symbol_text = symbol_element.string
            if symbol_text.startswith(ticker):
                symbol_count += 1
    
    # Close the webdriver
    driver.quit()
    
    # Print the result
    print(f"'{ticker}' was mentioned '{symbol_count}' times in the last '{interval}' minutes.")


# Example inputs
twitter_accounts = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox"
]

ticker = "$TSLA"  # Ticker symbol to look for
repeat_interval = 15 # Repeat every 15 minutes

while True:
    # Call the scraping function
    scrape_twitter_accounts(twitter_accounts, ticker, repeat_interval)
    
    # Wait for the specified interval before repeating
    time.sleep(repeat_interval * 60)  # Convert minutes to seconds
