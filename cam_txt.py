import requests
from bs4 import BeautifulSoup
import os

def eh_sujeito(txt):
    return txt[:6] == 'A SRA.' or txt[:5] == 'O SR.'


def main():
    global pasta 
    pasta= 'camara'
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    with open('codigos_camara.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            escrever(int(line))





def escrever(codigo):
    url = f'https://escriba.camara.leg.br/escriba-servicosweb/html/{codigo}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        arquivo = os.path.join(pasta, f'{codigo}.txt')
        with open(arquivo, 'w', encoding='utf-8') as file: 
            # Find all elements that contain the speaker and speech
            elements = soup.find("table") 
            quartos = elements.find_all('div', class_ = 'principalStyle')
            #print(quarto)
            for quarto in quartos:
                #Achar todos os politcos que falam
                sujeitos = quarto.find_all('a')
                for sujeito in sujeitos:
                    obj = sujeito.text.strip()
                    if eh_sujeito(obj):
                        #file.write(f"troca {sujeito.text.strip()}: \n")
                        file.write(f"\n")
                #Achar todas as falas
                falas = quarto.find_all('span')
                for fala in falas:
                    file.write(fala.get_text())
        
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    main()