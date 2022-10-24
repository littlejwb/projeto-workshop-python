import bs4
import requests

r = requests.get('https://filmow.com/filmes-todos/?order=saw&filters=&apply=')

html = r.text

soup = bs4.BeautifulSoup(html, 'html.parser')

print('Os filmes mais assistidos da plataforma são:')

for filmes in soup.findAll('span', {'class':'title'}):
        filmes = filmes.string
        print(filmes)

