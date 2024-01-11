import requests
from bs4 import BeautifulSoup
import csv

def scrape_leetcode_problems():
    url = 'https://leetcode.com/problemset/all/'

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

     problems = soup.find_all('div', class_='reactable-data-row')

        data = []

        for problem in problems:
            title = problem.find('div', class_='question-title').text.strip()
            difficulty = problem.find('span', class_='difficulty').text.strip()
            tags = [tag.text.strip() for tag in problem.find_all('a', class_='reactable-data')]

          
            problem_url = f"https://leetcode.com{problem.find('a', class_='reactable-data').get('href')}"
            problem_statement = get_problem_statement(problem_url)

            data.append({'Title': title, 'Difficulty': difficulty, 'Tags': tags, 'Problem Statement': problem_statement})

        save_to_csv(data)
        print('Scraping and CSV creation completed successfully.')

    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def get_problem_statement(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        statement = soup.find('div', class_='content__u3I1 question-content__JfgR')

        return statement.text.strip() if statement else 'Problem statement not available'

    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return 'Problem statement not available'

def save_to_csv(data):
    try:
        with open('leetcode_problems.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Difficulty', 'Tags', 'Problem Statement']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

            csv_writer.writeheader()
            csv_writer.writerows(data)

    except IOError as e:
        print(f"Error writing to CSV: {e}")

       
        print(response.text) 
        print(problems)  

scrape_leetcode_problems()
