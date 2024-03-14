import requests
import pandas as pd
from bs4 import BeautifulSoup

def requisicao():
    url = "https://localconncet.000webhostapp.com/Templates/showuser.php"

    response = requests.get(url)
    return response.text

def coletando_dados(html):
    soup = BeautifulSoup(html, "html.parser")

    rows = soup.find_all("tr")

    nomes = []
    cidades = []
    estados = []
    for row in rows[1:]:

        nome_td = row.find("td", id="nome")
        cidade_td = row.find("td", id="cidade")
        estado_td = row.find("td", id="estado")


        nome = nome_td.get_text(strip=True) if nome_td else ""
        cidade = cidade_td.get_text(strip=True) if cidade_td else ""
        estado = estado_td.get_text(strip=True) if estado_td else ""

        nomes.append(nome)
        cidades.append(cidade)
        estados.append(estado)


    df = pd.DataFrame({
        "Nome": nomes,
        "Cidade": cidades,
        "Estado": estados
    })


    df.to_csv("localconnectusers.csv", index=False)

    print("Os dados foram salvos em 'localconnectusers.csv'.")
    #debugando
    print(df.head())



if __name__ == '__main__':
    html = requisicao()
    coletando_dados(html)
