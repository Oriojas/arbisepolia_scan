import os
import pandas as pd
import arbi_connection as ab
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ.get('KEY')
URL = os.environ.get('SEPOLIA_URL')

df_faucet = pd.read_csv('/home/oscar/Github/arbisepolia_scan/data_raw/data_sepolia4.csv',
                        index_col=False)

df_result = pd.DataFrame()

for hash_id in df_faucet['Txhash']:
    print(hash_id)
    try:
        temp_resp = ab.ArbiSepScanner(key=KEY, url=URL).transaction_hash(t_hash=hash_id)
    except:
        temp_resp = {"status": "1",
                     "message": "OK",
                     "result": [
                                    {
                                        "blockNumber": "0",
                                        "timeStamp": "0",
                                        "from": "0",
                                        "to": "0",
                                        "value": "0",
                                        "contractAddress": "0",
                                        "input": "0",
                                        "type": "0",
                                        "gas": "0",
                                        "gasUsed": "0",
                                        "isError": "0",
                                        "errCode": "0"
                                    }
                                ]
                     }

    df_temp = pd.DataFrame(temp_resp['result'])
    print(df_temp)
    df_result = pd.concat([df_result, df_temp])

df_result.to_csv('/home/oscar/Github/arbisepolia_scan/output_data/txlistinternal6.csv')

