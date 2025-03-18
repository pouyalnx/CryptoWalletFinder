from web3 import Web3
import json


with open('erc20_abi.json') as f:
    abi=json.load(f)

w3=Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
w3.eth.account.enable_unaudited_hdwallet_features()
account=w3.eth.account.from_mnemonic("sauce labor food provide hunt innocent galaxy point admit innocent soul almost")
print(account.address)



#print(w3.eth.get_balance(account.address))
token = w3.eth.contract(address="0x5033833c9fe8B9d3E09EEd2f73d2aaF7E3872fd1", abi=abi) # declaring the token contract
print(token.functions.name().call())
#token_balance = token.functions.balanceOf(account.address).call()