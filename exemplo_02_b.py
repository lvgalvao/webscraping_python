import requests
from datetime import datetime
import os

# URL do produto
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Headers para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Faz a requisição
resposta = requests.get(url, headers=headers)

# Gera o timestamp para o nome do arquivo
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Garante que exista a pasta "htmls"
os.makedirs("htmls", exist_ok=True)

# Define o nome do arquivo com base no timestamp
filename = f"htmls/nintendo_switch_{timestamp}.html"

# Salva o HTML da resposta
with open(filename, "w", encoding="utf-8") as f:
    f.write(resposta.text)

print(f"✅ HTML salvo em: {filename}")
