from playwright.sync_api import sync_playwright
import time

URL = "https://www.skyscanner.com.br/transporte/passagens-aereas/slz/rioa/250728/250804/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&ref=home&rtn=1&stops=!direct,!twoPlusStops"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # use headless=True para rodar em segundo plano
        context = browser.new_context()
        page = context.new_page()

        print("Acessando o Skyscanner...")
        page.goto(URL)

        print("Aguardando os resultados carregarem...")
        page.wait_for_selector('[data-test-id="listing-card"]', timeout=60000)  # espera até 60 segundos

        cards = page.query_selector_all('[data-test-id="listing-card"]')

        print(f"\nForam encontrados {len(cards)} voos:\n")

        for card in cards:
            try:
                price = card.query_selector('[data-test-id="price"]').inner_text()
                airline = card.query_selector('[data-test-id="airline-name"]').inner_text()
                departure_time = card.query_selector('[data-test-id="departure-time"]').inner_text()
                arrival_time = card.query_selector('[data-test-id="arrival-time"]').inner_text()

                print(f"🛫 {airline}: {departure_time} → {arrival_time} | 💸 {price}")
            except:
                continue

        browser.close()

if __name__ == "__main__":
    run()
