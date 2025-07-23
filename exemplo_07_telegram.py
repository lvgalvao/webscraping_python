import requests

# Substitua pelos seus dados
token = "8499599956:AAHqSP_r_IfyKTMkV4ZX_-XeG7oujrOJPFo"

# https://api.telegram.org/bot8499599956:AAHqSP_r_IfyKTMkV4ZX_-XeG7oujrOJPFo/getUpdates
chat_id = "6852371789"  # Substitua pelo seu chat_id real

mensagem = "👋 Olá, Luciano! Seu bot do Telegram está funcionando."

# Monta a URL da API
url = f"https://api.telegram.org/bot{token}/sendMessage"

# Monta o payload da requisição
payload = {
    "chat_id": chat_id,
    "text": mensagem
}

# Envia a requisição
resposta = requests.post(url, data=payload)

# Verifica o status
if resposta.status_code == 200:
    print("✅ Mensagem enviada com sucesso!")
else:
    print("❌ Erro ao enviar:", resposta.text)
