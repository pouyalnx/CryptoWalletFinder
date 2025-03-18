from solana.rpc.api import Client


http_client = Client("https://rpc.ankr.com/solana")
http_client.get_balance('FFrGf6bA2iB8Szhr5tg3ESTmaPHPLnbhVcmX2VJ6nq4d')









"""
from mnemonic import Mnemonic
mne=Mnemonic('english')


from web3 import Web3
rpc="https://rpc.ankr.com/solana"
web3 = Web3(Web3.HTTPProvider(rpc))
print(web3.is_connected())
web3.eth.account.enable_unaudited_hdwallet_features()

for _ in range(16):
    words=mne.generate()
    account=web3.eth.account.from_mnemonic(words)
    address=account.address
    balance = web3.eth.get_balance(address)
    print("wallet:<",words,"> balance: ",balance)
"""