import requests
from bs4 import BeautifulSoup

url = 'https://escriba.camara.leg.br/escriba-servicosweb/html/75070'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        text = link.text.strip()
        #print(f"Link Text: {text}, URL: {href}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
'''busca: html -> body -> div -> div(id="contentEncontro") -> table (id = tabelaQuadros) 
-> tbody -> tr (quartos) -> td "justificado" -> segundo div -> span (vao conter os paragrafos) 
-> <b> -> <a> (vão conter os nomes dos sujeitos)
'''
print(soup.find_all('a'))
