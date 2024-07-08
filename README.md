
# Web Scraper for News Headlines
This project is a simple web scraper that fetches news headlines from a specified URL and saves them to a CSV file.

## Features
- Command-line interface (CLI) for ease of use
- Logging to track the scraping process
- Error handling for robustness
- Saves scraped data to a CSV file with website URL and headline

## Requirements
- Python 3.x
- `beautifulsoup4` library
- `requests` library

## Installation
1. Clone the repository:
    git clone https://github.com/yourusername/web_scraper.git
    cd web_scraper


2. Install the required libraries:
    pip install -r requirements.txt

## Usage
Run the script with the URL of the news website you want to scrape:
python scraper.py 'https://timesofindia.indiatimes.com/' -o output.csv ## Example
