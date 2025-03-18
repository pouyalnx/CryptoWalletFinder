
from web3 import Web3

abi = [{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"},{"internalType":"uint256[]","name":"balances","type":"uint256[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
usdt_ct=Web3.to_checksum_address("0xdac17f958d2ee523a2206206994597c13d831ec7")
dai_ct=Web3.to_checksum_address("0x6b175474e89094c44da98b954eedeac495271d0f")
shiba_ct=Web3.to_checksum_address("0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce")
mantle_ct=Web3.to_checksum_address("0x3c3a81e81dc49a522a592e7622a7e711c06bf354")
arbitrum_ct=Web3.to_checksum_address("0x912CE59144191C1204E64559FE8253a0e49E6548")
sandbox_ct=Web3.to_checksum_address("0x3845badAde8e6dFF049820680d1F14bD3903a5d0")
fdusd_ct=Web3.to_checksum_address("0xc5f0f7b66764F6ec8C8Dff7BA683102295E16409")
usdcoin_ct=Web3.to_checksum_address("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
toncoin_ct=Web3.to_checksum_address("0x582d872a1b094fc48f5de31d3b73f2d9be47def1")
polygon_ct=Web3.to_checksum_address("0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0")
trueusd_ct=Web3.to_checksum_address("0x0000000000085d4780B73119b644AE5ecd22b376")


infura_url = "https://rpc.ankr.com/eth"
web3 = Web3(Web3.HTTPProvider(infura_url))


usdt=web3.eth.contract(address=usdt_ct,abi=abi)
dai=web3.eth.contract(address=dai_ct,abi=abi)
shiba=web3.eth.contract(address=shiba_ct,abi=abi)
mantle=web3.eth.contract(address=mantle_ct,abi=abi)
arbitrum=web3.eth.contract(address=arbitrum_ct,abi=abi)
sandbox=web3.eth.contract(address=sandbox_ct,abi=abi)
fdusd=web3.eth.contract(address=fdusd_ct,abi=abi)
usdcoin=web3.eth.contract(address=usdcoin_ct,abi=abi)
toncoin=web3.eth.contract(address=toncoin_ct,abi=abi)
polygon=web3.eth.contract(address=polygon_ct,abi=abi)
trueusd=web3.eth.contract(address=trueusd_ct,abi=abi)

def get_balance(address):
    print("eth=",web3.eth.get_balance(address))
    print("usdt=",usdt.functions.balanceOf(address).call())
    print("dai=",dai.functions.balanceOf(address).call())
    print("shiba=",shiba.functions.balanceOf(address).call())
    print("mantle=",mantle.functions.balanceOf(address).call())
#    print("arbitrum=",arbitrum.functions.balanceOf(address).call())
    print("sandbox=",sandbox.functions.balanceOf(address).call())
    print("fdusd=",fdusd.functions.balanceOf(address).call())
    print("usdcoin=",usdcoin.functions.balanceOf(address).call())
    print("toncoin=",toncoin.functions.balanceOf(address).call())
    print("polygon=",polygon.functions.balanceOf(address).call())
    print("trueusd=",trueusd.functions.balanceOf(address).call())

get_balance("0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3")


"""
    print("eth=",web3.eth.get_balance(address))
    print("usdt=",usdt.functions.name().call())
    print("dai=",dai.functions.name().call())
    print("shiba=",shiba.functions.name().call())
    print("mantle=",mantle.functions.name().call())
#    print("arbitrum=",arbitrum.functions.name().call())
    print("sandbox=",sandbox.functions.name().call())
    print("fdusd=",fdusd.functions.name().call())
    print("usdcoin=",usdcoin.functions.name().call())
    print("toncoin=",toncoin.functions.name().call())
    print("polygon=",polygon.functions.name().call())
    print("trueusd=",trueusd.functions.name().call())
"""