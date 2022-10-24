import requests

r = requests.get('https://filmow.com/filmes-todos/?order=saw&filters=&apply=')

html = r.text.split('\n')

print('Os filmes mais assistidos da plataforma são:')

for filmes in html:
    if '<h3><span class="title">' in filmes:
        filmes = filmes.replace('<h3><span class="title">', '')
        filmes = filmes.replace('</span></h3>','')
        print(filmes)
