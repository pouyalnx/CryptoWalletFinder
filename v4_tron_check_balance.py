from tronpy import Tron
import requests
import json

class TRC20:
    def __init__(self):
        self.client = Tron()
    
    def get_balance(self,mnemonic):
        acc=self.client.generate_address_from_mnemonic(mnemonic)
        address=acc['base58check_address']
        url = "https://apilist.tronscan.org/api/account"
        payload = {
            "address": address,
        }
        res = requests.get(url, params=payload)
        tokens=json.loads(res.text)["tokenBalances"]
        balance={}
        for token in tokens:
            balance[token['tokenName']]=token['balance']
        return balance


mne="sauce labor food provide hunt innocent galaxy point admit innocent soul almost"

trc=TRC20()
print(trc.get_balance(mne))