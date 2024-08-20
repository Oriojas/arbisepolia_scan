import requests


class CeloAlfScanner(object):

    def __init__(self, key):
        self.key = key

    def transaction_address(self, address):
        url = (f"https://api.celoscan.io/api"
               f"?module=account"
               f"&action=txlist"
               f"&address={address}"
               f"&startblock=0"
               f"&endblock=99999999"
               f"&page=1"
               f"&offset=10"
               f"&sort=asc"
               f"&apikey={self.key}")

        response = requests.get(url)

        return response.json()

    def transaction_hash(self, t_hash):
        url = (f"https://api.celoscan.io/api"
               f"?module=account"
               f"&action=txlistinternal"
               f"&txhash={t_hash}"
               f"&apikey={self.key}")

        response = requests.get(url)

        return response.json()
