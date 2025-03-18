from web3 import Web3
import time, json
bsc = 'https://bsc-dataseed.binance.org/'
#bsc="https://rpc.ankr.com/eth"
#bsc="https://rpc.ankr.com/bsc"
#bsc="https://rpc.ankr.com/http/tron" //cant work
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.is_connected())


web3.eth.account.enable_unaudited_hdwallet_features()
account=web3.eth.account.from_mnemonic("sauce labor food provide hunt innocent galaxy point admit innocent soul almost")
print(account.address)
address=account.address  #'0xd6A12c6B1632D60ff4813CF3BC75dfD0118Cdedf'
balance = web3.eth.get_balance(address)
print(balance)
 
result = web3.from_wei(balance,'ether')
print(result)