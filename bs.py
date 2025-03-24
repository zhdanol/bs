import bs4
import requests


## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

## Ваш код
response = requests.get('https://habr.com/ru/articles/')
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('articles', class_='tm-svg-img tm-header__icon')

for article in articles:
    hubs = article.find_all('a', class_ = 'tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    print(hubs)
    date = article.find('time').text
    title = article.find('a', class_ = 'tm-article-snippet__title-link')
    span_title = title.find('span').text
    print(span_title)
    
    
    if KEYWORDS & hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок:{title} - Ссылка: {url}')