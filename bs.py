from bs4 import BeautifulSoup
import requests
from fake_headers import Headers
from pprint import pprint
headers=Headers(browser='chrome', os='mac').generate()


## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

## Ваш код
response = requests.get('https://habr.com/ru/articles/')


if response.status_code != 200:
    print(f"Ошибка при запросе: {response.status_code}")
    
with open('index.html','w',encoding='utf-8') as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
articles = []

for article in soup.find_all('article', class_ = 'tm-article-snippet__hubs-item-link'):
    try:
        title_tag = article.find_all('h2', class_ = 'tm-title')
        title = title_tag.text.strip()
        link = "https://habr.com" + title_tag.find('a')['href']
        
        date_tag = article.find('time')
        date = date_tag['title'] if date_tag else "Дата не указана"
        
        summary_tag = article.find('div', class_= 'article-formatted-body')
        summary = summary_tag.text.lower() if summary_tag else ""
        
        if any(keyword.lower() in summary for keyword in KEYWORDS):
            articles.append({
                "title": title,
                "date": date,
                "link": link
            })
    except Exception as e:
        print(f"Ошибка при обработке статьи: {e}")
pprint(articles)
