import requests

class ArbiOneScanner(object):

    def __init__(self, key):
        self.key = key


    def transaction_hash(self, hash):
        url = (f"https://api.arbiscan.io/api"
               f"?module=account"
               f"&action=txlistinternal"
               f"&txhash={hash}"
               f"&apikey={self.key}")

        response = requests.get(url)

        return response.json()

if __name__ == "__main__":
    transaction = ArbiOneScanner(key="8DXKZIKYAHBCFZUN5IZM2VRNW7C89FS61I").transaction_hash(hash="0x5e2ce795c7c184ea26cc64550ae5f0c2cfd7ff14c6b932bac0b2eaa278ccc522")
    print(transaction)