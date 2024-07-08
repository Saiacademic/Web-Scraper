import requests
from bs4 import BeautifulSoup
import logging
import argparse
from utils import save_to_csv

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_news(url, output_file):
    try:
        # Send a request to the website
        logging.info(f"Fetching content from {url}")
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Define possible tags and classes for headlines
        headline_tags = [
            ('h1', None),
            ('h2', None),
            ('h3', None),
            ('span', 'w_tle'),
            ('a', 'w_img')
        ]

        data = []
        for tag, class_name in headline_tags:
            if class_name:
                headlines = soup.find_all(tag, class_=class_name)
            else:
                headlines = soup.find_all(tag)

            for headline in headlines:
                headline_text = headline.get_text(strip=True)
                # Avoid duplicates
                if headline_text and headline_text not in [item['headline'] for item in data]:
                    data.append({'website': url, 'headline': headline_text})

        if data:
            # Save to CSV
            save_to_csv(data, output_file)
            logging.info(f"Headlines saved to {output_file}")
        else:
            logging.warning("No headlines found to save.")

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Web Scraper for News Headlines")
    parser.add_argument('url', help="URL of the news website to scrape")
    parser.add_argument(
        '-o', '--output', default='headlines.csv', help="Output CSV file")
    args = parser.parse_args()

    fetch_news(args.url, args.output)
