import csv
from datetime import datetime, timedelta
import random
import time

# Parâmetros da simulação
nome_produto = "Console Nintendo Switch 2 Preto"
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061"
data_source = "Mercado Livre"

# Geração de timestamps a cada minuto nos últimos 3 dias
inicio = datetime.now() - timedelta(days=3)
fim = datetime.now()
intervalo = timedelta(minutes=60)

# Lista de preços simulados (base entre 1800 e 2300)
def gerar_preco():
    return random.randint(1800, 2300)

# Abrir o CSV para escrita
with open("historico_precos_fake.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    tempo_atual = inicio

    while tempo_atual <= fim:
        preco = gerar_preco()
        row = [
            tempo_atual.strftime("%Y-%m-%d %H:%M:%S"),
            nome_produto,
            preco,
            url,
            data_source
        ]
        writer.writerow(row)
        tempo_atual += intervalo

print("✅ Simulação concluída: dados salvos em historico_precos_fake.csv")
