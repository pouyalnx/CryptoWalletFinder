from mnemonic import Mnemonic
mne=Mnemonic('english')


from web3 import Web3
rpc_server="https://data-seed-prebsc-1-s1.binance.org:8545"
web3 = Web3(Web3.HTTPProvider(rpc_server))
print(web3.is_connected())
web3.eth.account.enable_unaudited_hdwallet_features()

for _ in range(16):
    words=mne.generate()
    account=web3.eth.account.from_mnemonic(words)
    address=account.address
    balance = web3.eth.get_balance(address)
    print("wallet:<",words,"> balance: ",balance)
 