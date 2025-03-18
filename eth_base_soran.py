"0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"
"bc1qmll3fcxy28gq97svl3chh93addgwwz3jnvkj7p"

from web3 import Web3
import time, json
#bsc = 'https://bsc-dataseed.binance.org/'
bsc="https://rpc.ankr.com/eth"
bsc="https://rpc.ankr.com/bsc"
#bsc="https://rpc.ankr.com/http/tron" //cant work
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.is_connected())

address="0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"  #'0xd6A12c6B1632D60ff4813CF3BC75dfD0118Cdedf'
balance = web3.eth.get_balance(address)
print(balance)
 
result = web3.from_wei(balance,'ether')
print(result)