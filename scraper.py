import requests
from bs4 import BeautifulSoup
from newspaper import Article
from tqdm import tqdm
import pandas as pd

def repetitive(links, urls):
    for link in links:
        if link.a['href'] in urls:
            return True
    return False

def scrap_year():
    news_number = 5447
    scraped_data = []
    url_list = []

    while True:
        news_number -= 1

        main_page_url = f"https://donya-e-eqtesad.com/%D8%A8%D8%AE%D8%B4-%D8%AE%D8%A8%D8%B1-64?np={news_number}"

        html = requests.get(main_page_url).text  # Download html of the page

        soup = BeautifulSoup(html, features='lxml')
    
        links = soup.find_all('h2')
        print(links)
        if repetitive(links, url_list):
            break

        for link in tqdm(links):
            page_url = 'https://donya-e-eqtesad.com/' + link.a['href']
            url_list.append(link.a['href'])
            try:
                article = Article(page_url)
                article.download()
                article.parse()
                scraped_data.append({'url': page_url, 'text': article.text, 'title': article.title})
            except:
                print(f"Failed to process page: {page_url}")    
    df = pd.DataFrame(scraped_data)
    df.to_csv(f'news_data.csv')


if __name__ == '__main__':
    scrap_year()
