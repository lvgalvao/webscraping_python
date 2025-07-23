import requests                      # Faz a requisição HTTP
from bs4 import BeautifulSoup        # Faz o parsing do HTML
from datetime import datetime        # Para gerar a data atual
import csv                           # Para salvar os dados no CSV

# URL do produto que será monitorado
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Cabeçalhos para simular um navegador real (evita bloqueios)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Faz a requisição HTTP para a página do produto
resposta = requests.get(url, headers=headers)

# Faz o parsing da resposta HTML usando o BeautifulSoup
soup = BeautifulSoup(resposta.text, "html.parser")

# Tenta localizar o preço na página pelo seletor CSS
preco_elemento = soup.select_one("span.andes-money-amount__fraction")

if preco_elemento:
    # Remove espaços em branco e salva o valor como string
    preco = preco_elemento.text.strip()

    # Nome do produto (simulado aqui, mas poderia ser extraído via soup também)
    nome_produto = "Console Nintendo Switch 2 Preto"

    # Data/hora da coleta
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Fonte dos dados
    data_source = "Mercado Livre"

    # Salva os dados em um arquivo CSV (modo append)
    with open("historico_precos.csv", "a", newline="") as arquivo_csv:
        writer = csv.writer(arquivo_csv)

        # Linha de dados completa
        writer.writerow([created_at, nome_produto, preco, url, data_source])

    print(f"✅ Preço salvo: R$ {preco} | {created_at}")
else:
    print("❌ Preço não encontrado")
