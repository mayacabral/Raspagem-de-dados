import requests
from bs4 import BeautifulSoup


url = 'https://www.idealsoftwares.com.br/indices/ipca_ibge.html'

response = requests.get(url)
html_content = response.content

Beauti = BeautifulSoup(html_content, 'html.parser')

soup = Beauti.find_all(
    name='table', 
    attrs={'class': 'table table-bordered table-striped text-center'}
)

texto = soup[0]
#print(soup.prettify()[:3000])

ipca_data = []
for row in texto.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols: 
        data = cols[0].text.strip()
        valor = cols[1].text.strip().replace(',', '.').replace(' ', '').replace('/n', '')
        if valor:
            ipca_data.append((data, valor))

print(ipca_data)