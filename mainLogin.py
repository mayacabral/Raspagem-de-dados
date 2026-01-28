import requests
from bs4 import BeautifulSoup


login_url = 'https://loja.rigrantec.com.br'

session = requests.Session()

session.get(login_url)
token = session.cookies.get("autorizacao")


login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')

csrf_token = soup.find(
    'input', 
    {'name': 'csrf_token'}
    
).get('value')