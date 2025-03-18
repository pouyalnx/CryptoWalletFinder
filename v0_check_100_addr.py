from mnemonic import Mnemonic
mne=Mnemonic('english')


from web3 import Web3
#hp = 'https://bsc-dataseed.binance.org/'
hp="https://rpc.ankr.com/eth"
web3 = Web3(Web3.HTTPProvider(hp))
print(web3.is_connected())
web3.eth.account.enable_unaudited_hdwallet_features()

for _ in range(16):
    words=mne.generate()
    account=web3.eth.account.from_mnemonic(words)
    address=account.address
    balance = web3.eth.get_balance(address)
    print("wallet:<",words,"> balance: ",balance)
 