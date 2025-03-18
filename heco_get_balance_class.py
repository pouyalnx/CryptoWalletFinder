###########################################################################################################
from web3 import Web3

class HECO:
    def __init__(self,prc_provider=None) -> None:
        print("-----------------HECO---------------")
        if prc_provider==None:
            prc_provider="https://http-mainnet.hecochain.com"

        self.web3=Web3(Web3.HTTPProvider(prc_provider))
        print("connecting...")
        if self.web3.is_connected()==False:
            print("Error:Unable Connect to Prc")

        print("converting tokens address...")
        self.abi = [{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"},{"internalType":"uint256[]","name":"balances","type":"uint256[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
        self.polkadot_ct=Web3.to_checksum_address("0xa2c49cee16a5e5bdefde931107dc1fae9f7773e3")
        self.bitcoincash_ct=Web3.to_checksum_address("0xef3cebd77e0c52cb6f60875d9306397b5caca375")
        self.filecoin_ct=Web3.to_checksum_address("0xae3a768f9ab104c69a7cd6041fe16ffa235d1810")

        print("adding contracts...")
        self.polkadot=self.web3.eth.contract(self.polkadot_ct,abi=self.abi)
        self.bitcoincash=self.web3.eth.contract(self.bitcoincash_ct,abi=self.abi)
        self.filecoin=self.web3.eth.contract(self.filecoin_ct,abi=self.abi)
  

        print("querry names....")
        self.heco_name="HECO"
        print(self.heco_name," OK!")
        self.polkadot_name=self.polkadot.functions.name().call()
        print(self.polkadot_name," OK!")
        self.bitcoincash_name=self.bitcoincash.functions.name().call()
        print(self.bitcoincash_name," OK!")
        self.filecoin_name=self.filecoin.functions.name().call()
        print(self.filecoin_name," OK!")


        print("init completed.")


    def get_balance(self,address):
        balance={}
        balance[self.heco_name]=self.web3.eth.get_balance(address)
        balance[self.polkadot_name]=self.polkadot.functions.balanceOf(address).call()
        balance[self.bitcoincash_name]=self.bitcoincash.functions.balanceOf(address).call()
        balance[self.filecoin_name]=self.filecoin.functions.balanceOf(address).call()

        return balance

    def is_have_balance(self,address):
        if(self.web3.eth.get_balance(address)!=0):
            return True
        if(self.polkadot.functions.balanceOf(address).call()!=0):
            return True
        if(self.bitcoincash.functions.balanceOf(address).call()!=0):
            return True
        if(self.filecoin.functions.balanceOf(address).call()!=0):
            return True
        return False


####################################################################################################################
from web3 import Web3
web3 = Web3()

from mnemonic import Mnemonic
mne=Mnemonic('english')

bep20=HECO()

web3.eth.account.enable_unaudited_hdwallet_features()
for _ in range(32):
    words=mne.generate()
    account=web3.eth.account.from_mnemonic(words)
    print("mnemonic:<",words,">")
    print(bep20.get_balance(account.address))

    print("----------------------------------------------------------------")


