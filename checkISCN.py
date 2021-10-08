import requests
import json

endpoint='https://mainnet-node.like.co/txs?message.module=iscn'

resp = requests.get(endpoint,timeout=(60,120))

returnedDict = json.loads(resp.text)

print(f"keys of the returned json: {str(returnedDict.keys())}")
print(f"total ISCN count:{returnedDict['total_count']}")
