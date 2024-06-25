import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data_points = []
        for item in soup.find_all('div', class_='mw-category'):
            data_points.append(item.text.strip())
        return data_points
    else: 
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def save_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])

if __name__ == "__main__":
    target_url = 'https://en.wikipedia.org/wiki/Category:Python_(programming_language)'
    scraped_data = scrape_website(target_url)
    if scraped_data:
        csv_file = 'scraped_data.csv'
        save_to_csv(scraped_data, csv_file)
        print(f"Scraped data has been saved to {csv_file}")
    else:
        print("Scraping failed.")
