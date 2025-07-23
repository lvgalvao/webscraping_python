import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

resposta = requests.get(url, headers=headers)
soup = BeautifulSoup(resposta.text, "html.parser")

preco_elemento = soup.select_one("span.andes-money-amount__fraction")

if preco_elemento:
    preco = preco_elemento.text.strip()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Salva no CSV
    with open("historico_precos.csv", "a", newline="") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([data_hora, preco])
    
    print(f"💰 Preço capturado: R$ {preco} | Salvo em historico_precos.csv")
else:
    print("❌ Preço não encontrado")
