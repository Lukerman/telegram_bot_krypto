import requests
import json

def lisa_valinta(valuutta, valinta):

    user_message = str(valuutta).lower()

    url = "https://api.coingecko.com/api/v3/coins/" + user_message
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()
            tilasto = data['market_data'][valinta]['eur']
            return "\n" + valinta + ": " + tilasto + '€'
        except Exception as e:
            print(e)
            return "\nVäärä lisävalinta \"" + valinta + "\" :(."


def krypto(teksti):
    user_message = str(teksti).lower()

    if user_message == "eth" or user_message == "etukka":
        user_message = "ethereum"
    if user_message == "btc":
        user_message = "bitcoin"
    if user_message == "cfx" or user_message == "conflux":
        user_message = "conflux-token"
    if user_message == "snx" or user_message == "synthetix":
        user_message = "havven"

    url = "https://api.coingecko.com/api/v3/coins/" + user_message
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()
            kuvaus = user_message + " hinta:\n"
            hinta = float(data['market_data']['current_price']['eur'])
            suunta_24h = float(data['market_data']['price_change_percentage_1h_in_currency']['eur'])
            teksti_hinta = str(hinta) + "€\n"
            teksti_suunta = "{:.2f}% 24h".format(suunta_24h)

            return kuvaus + teksti_hinta + teksti_suunta
        except Exception as e:
            print(e)
            return "Väärä syöte :(."

def louhinta(teksti, hashit):

    user_message = str(teksti).lower()

    url = "https://api.minerstat.com/v2/coins?list=" + user_message
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()
            tuotto_krypto = float(data[0]['reward']) * hashit*10**6 * 24
            tuotto_usd = tuotto_krypto * data[0]['price']
            kuvaus_teksti = "24h tuotto " + str(hashit) + "Mh/s:\n"
            teksti_krypto = "{:.5f} ".format(tuotto_krypto) + user_message + "\n"
            teksti_usd = "{:.2f} $".format(tuotto_usd)
            return kuvaus_teksti + teksti_krypto + teksti_usd
        except Exception as e:
            print(e)
            return "Error"


def osake(teksti):
    user_message = str(teksti).lower()

    url = "https://api.twelvedata.com/price?symbol=" + user_message + "&apikey=7ff27d2112734a9abd57b2bfff22f688"
    r = requests.get(url)

    if r.status_code == 200:
        try:
            data = r.json()
            print(data['price'])
            kuvaus = "Osakkeen hinta:\n"
            hinta_osake = float(data['price'])
            teksti_osake = "{:.2f} $".format(hinta_osake)
            return kuvaus + teksti_osake
        except Exception as e:
            print(e)
            return "Väärä valinta, tai liikaa yrityksiä"
