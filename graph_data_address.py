import os
import pandas as pd
import arbi_connection as ab
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ.get('KEY')
URL = os.environ.get('SEPOLIA_URL')

df_faucet = pd.read_csv('/home/oscar/Github/arbisepolia_scan/output_data/txlistinternal6.csv',
                        index_col=False)

df_faucet = df_faucet.drop_duplicates(subset='to')

df_result = pd.DataFrame()

for address in df_faucet['to']:
    print(address)
    try:
        temp_resp = ab.ArbiSepScanner(key=KEY, url=URL).transaction_address(address=address)
    except:
        temp_resp = {
                      "status": "1",
                      "message": "OK",
                      "result": [
                        {
                          "blockNumber": "23264575",
                          "blockHash": "0x4022a3b43042ce38d08f71d96cabe7bf16426e3881326d0f7bbf56c9ddef31bb",
                          "timeStamp": "1710458753",
                          "hash": "0xcbd0b4a6e9bb98200ccf1a16d5ca58237f2c2c32a4756b025d89db3df2f9bb50",
                          "nonce": "112459",
                          "transactionIndex": "2",
                          "from": "0x87c9b02a10ec2cb4dcb3b2e573e26169cf3cd9bf",
                          "to": "0x1d870f1210e66cba98093682b84d4491ec04141b",
                          "value": "500000000000000000",
                          "gas": "741798",
                          "gasPrice": "300000000",
                          "input": "0x",
                          "methodId": "0x",
                          "functionName": "",
                          "contractAddress": "",
                          "cumulativeGasUsed": "1005392",
                          "txreceipt_status": "1",
                          "gasUsed": "183928",
                          "confirmations": "18678057",
                          "isError": "0"
                        }
                      ]
                    }

    df_temp = pd.DataFrame(temp_resp['result'])
    df_temp['address'] = address
    print(df_temp)
    df_result = pd.concat([df_result, df_temp])

df_result.to_csv('/home/oscar/Github/arbisepolia_scan/output_data/txlistaddres6.csv')

