import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = os.environ.get('ARBITRUM_URL')

class ArbiOneScanner(object):

    def __init__(self, key):
        self.key = key


    def transaction_hash(self, address):
        url = (f"{URL}"
               f"?module=account"
               f"&action=txlistinternal"
               f"&address={address}"
               f"&startblock=0"
               f"&endblock=99999999"
               f"&page=1"
               f"&offset=1000"
               f"&sort=asc"
               f"&apikey={self.key}")

        response = requests.get(url)

        return response.json()

if __name__ == "__main__":
    import json

    KEY = os.environ.get('KEY')
    MAIN_DIR = os.environ.get('MAIN_DIR')
    address_contract = "0x8c5ff04497062be94e59412163a2e771a8154beb"

    transaction = ArbiOneScanner(key=KEY).transaction_hash(address=address_contract)

    details_filename = os.path.join(f"{MAIN_DIR}/output_data", f"internal_tx_{address_contract}.json")
    with open(details_filename, 'w', encoding='utf-8') as f:
        json.dump(transaction, f, indent=4)

    print(transaction)