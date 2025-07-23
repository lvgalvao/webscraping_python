import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time
import random

# === Configurações do Telegram ===
token = "8499599956:AAHqSP_r_IfyKTMkV4ZX_-XeG7oujrOJPFo"
chat_id = "6852371789"
telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"

# === Configuração do scraping ===
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# === Preço alvo para enviar alerta
preco_alvo = 6000  # Altere aqui conforme sua meta

# === Loop infinito ===
while True:
    try:
        resposta = requests.get(url, headers=headers)
        soup = BeautifulSoup(resposta.text, "html.parser")
        preco_elemento = soup.select_one("span.andes-money-amount__fraction")

        if preco_elemento:
            preco_str = preco_elemento.text.strip()
            preco_int = int(preco_str.replace(".", "").replace(",", ""))  # Preço como número inteiro

            nome_produto = "Console Nintendo Switch 2 Preto"
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_source = "Mercado Livre"

            # Salvar no CSV
            with open("historico_precos.csv", "a", newline="") as arquivo_csv:
                writer = csv.writer(arquivo_csv)
                writer.writerow([created_at, nome_produto, preco_str, url, data_source])

            print(f"✅ Preço salvo: R$ {preco_str} | {created_at}")

            # Enviar alerta apenas se o preço for menor ou igual ao alvo
            if preco_int <= preco_alvo:
                mensagem = (
                    f"🚨 Oferta encontrada!\n\n"
                    f"📦 Produto: {nome_produto}\n"
                    f"💰 Preço: R$ {preco_str}\n"
                    f"📉 Alvo: R$ {preco_alvo}\n"
                    f"🕒 Coletado em: {created_at}\n"
                    f"🔗 {url}"
                )
                payload = {"chat_id": chat_id, "text": mensagem}
                response = requests.post(telegram_url, data=payload)

                if response.status_code == 200:
                    print("📲 Alerta enviado pelo Telegram.\n")
                else:
                    print("⚠️ Erro ao enviar mensagem:", response.text)

        else:
            print(f"❌ Preço não encontrado | {datetime.now().strftime('%H:%M:%S')}")

    except Exception as e:
        print(f"❗ Erro durante a execução: {e}")

    tempo_espera = random.randint(55, 65)
    print(f"⏳ Aguardando {tempo_espera} segundos para a próxima verificação...\n")
    time.sleep(tempo_espera)
