import requests

url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

resposta = requests.get(url)

print(resposta)