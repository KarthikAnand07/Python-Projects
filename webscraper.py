import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exception.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_article_titles(soup):
    titles = []
    for article in soup.find_all('h3', class_='page-title'):
        titles.append(article.get_text(strip=True))
    return titles

def main(url):
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        titles = extract_article_titles(soup)
        print("Article Titles: ")
        for title in titles:
            print(title)

if __name__ == "__main__":
    url = 'https://www.scrapethissite.com/pages/'
    main(url)
