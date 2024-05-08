import os
import pandas as pd
import arbi_connection as ab
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ.get('KEY')


temp_resp = ab.ArbiSepScanner(key=KEY).transaction_address(address="0x1d870f1210e66cba98093682b84d4491Ec04141b")



print(temp_resp)
