from web3 import Web3


w3=Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
w3.eth.account.enable_unaudited_hdwallet_features()
account=w3.eth.account.from_mnemonic("sauce labor food provide hunt innocent galaxy point admit innocent soul almost")
print(account.address)
print(account.key)



print(w3.eth.get_balance("0xd6A12c6B1632D60ff4813CF3BC75dfD0118Cdedf"))#"account.address))
#token = w3.eth.contract(address="0x5033833c9fe8B9d3E09EEd2f73d2aaF7E3872fd1", abi='[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"stateMutability":"payable","type":"fallback"},{"stateMutability":"payable","type":"receive"}]') # declaring the token contract
#token_balance = token.functions.balanceOf(account.address).call()