from web3 import Web3

w3=Web3()
w3.eth.account.enable_unaudited_hdwallet_features()
account=w3.eth.account.from_mnemonic("sauce labor food provide hunt innocent galaxy point admit innocent soul almost")
print(account.address)
print(account)