import requests
import json
import time

def get_crypto_prices(crypto_ids):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {crypto: data.get(crypto, {}).get("usd", "N/A") for crypto in crypto_ids}
    else:
        return f"Erreur {response.status_code}"

# Liste des cryptos
cryptos = ["bitcoin", "ethereum", "tether", "ripple", "binancecoin", "solana", "usd-coin", "cardano", "dogecoin", "tron"]

# Boucle infinie pour mettre à jour les prix toutes les minutes
while True:
    prices = get_crypto_prices(cryptos)
    
    # Sauvegarde dans un fichier JSON
    with open("prices.json", "w") as json_file:
        json.dump(prices, json_file, indent=4)
    
    print("Mise à jour des prix...")
    time.sleep(30)  # Attendre 60 secondes avant la prochaine requête
