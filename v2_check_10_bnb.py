from mnemonic import Mnemonic
mne=Mnemonic('english')


from web3 import Web3
hp = 'https://bsc-dataseed.binance.org/'
wbp20 = Web3(Web3.HTTPProvider(hp))
print(wbp20.is_connected())
wbp20.eth.account.enable_unaudited_hdwallet_features()

abi = [{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"},{"internalType":"uint256[]","name":"balances","type":"uint256[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
xrp_ct=Web3.to_checksum_address("0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe")
cardano_ct=Web3.to_checksum_address("0x3ee2200efb3400fabb9aacf31297cbdd1d435d47")
cosmos_ct=Web3.to_checksum_address("0x0eb3a705fc54725037cc9e008bdede697f62f335")
eth_classic_ct=Web3.to_checksum_address("0x3d6545b08693dae087e957cb1180ee38b9e3c25e")
zcash_ct=Web3.to_checksum_address("0x1ba42e5193dfa8b03d15dd1b86a3113bbbef8eeb")


xrp=wbp20.eth.contract(xrp_ct,abi=abi)
cardano=wbp20.eth.contract(cardano_ct,abi=abi)
cosmos=wbp20.eth.contract(cosmos_ct,abi=abi)
eth_classic=wbp20.eth.contract(eth_classic_ct,abi=abi)
zcash=wbp20.eth.contract(zcash_ct,abi=abi)


Bnb_name="BNB"
xrp_name=xrp.functions.name().call()
cardano_name=cardano.functions.name().call()
cosmos_name=cosmos.functions.name().call()
eth_classic_name=eth_classic.functions.name().call()
zcash_name=zcash.functions.name().call()

def get_balance(address):
    print(Bnb_name," = ",wbp20.eth.get_balance(address))
    print(xrp_name," = ",xrp.functions.balanceOf(address).call())
    print(cardano_name," = ",cardano.functions.balanceOf(address).call())
    print(cosmos_name," = ",cosmos.functions.balanceOf(address).call())
    print(eth_classic_name," = ",eth_classic.functions.balanceOf(address).call())
    print(zcash_name," = ",zcash.functions.balanceOf(address).call())






for _ in range(32):
    words=mne.generate()
    account=wbp20.eth.account.from_mnemonic(words)
    print("mnemonic:<",words,">")
    get_balance(account.address)
    print("----------------------------------------------------------------")


