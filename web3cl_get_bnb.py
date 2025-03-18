from web3factory.factory import make_client, make_erc20_client
address = "0x5FCcA657029DC096De515d2186E7fC8d7A009D28"
#address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
eth = make_client("eth").get_balance_in_eth(address)
usdc = make_erc20_client("USDC", "eth").balanceOf(address) / 10**6