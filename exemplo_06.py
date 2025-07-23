import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time
import random

# URL do produto que será monitorado
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Cabeçalhos para simular um navegador real (evita bloqueios)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

while True:
    try:
        # Faz a requisição HTTP para a página do produto
        resposta = requests.get(url, headers=headers)
        soup = BeautifulSoup(resposta.text, "html.parser")

        # Tenta localizar o preço na página pelo seletor CSS
        preco_elemento = soup.select_one("span.andes-money-amount__fraction")

        if preco_elemento:
            preco = preco_elemento.text.strip()
            nome_produto = "Console Nintendo Switch 2 Preto"
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_source = "Mercado Livre"

            # Salva os dados em um arquivo CSV
            with open("historico_precos.csv", "a", newline="") as arquivo_csv:
                writer = csv.writer(arquivo_csv)
                writer.writerow([created_at, nome_produto, preco, url, data_source])

            print(f"✅ Preço salvo: R$ {preco} | {created_at}")
        else:
            print(f"❌ Preço não encontrado | {datetime.now().strftime('%H:%M:%S')}")

    except Exception as e:
        print(f"❗ Erro durante a execução: {e}")

    # Espera entre 55 a 65 segundos para simular comportamento mais "humano"
    tempo_espera = random.randint(55, 65)
    print(f"⏳ Aguardando {tempo_espera} segundos para a próxima execução...\n")
    time.sleep(tempo_espera)
