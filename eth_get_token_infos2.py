from web3 import Web3, IPCProvider
import json
token_t_abi = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')


wallet_w ="0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"  # '0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE'

infura_url = "https://rpc.ankr.com/eth"

w3 = Web3(Web3.HTTPProvider(infura_url))

#w3 = Web3(IPCProvider())

token = w3.eth.contract(Web3.to_checksum_address('0xdac17f958d2ee523a2206206994597c13d831ec7'),abi=token_t_abi)

print(token.functions.balanceOf(wallet_w).call())