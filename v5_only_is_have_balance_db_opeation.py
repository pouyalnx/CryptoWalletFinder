from bitcoinlib.wallets import Wallet, wallet_delete_if_exists

class BTC:
    def __init__(self) -> None:
        self.__btc_name="BTC"
        self.__lte_name="LTE"
        self.__dash_name="dash"
        self.__doge_name="doge"

    def get_balance(self,mne):
        balance={}

        wallet_delete_if_exists(self.__btc_name)
        w = Wallet.create(self.__btc_name,keys=mne, network='bitcoin')
        balance["BTC"]=w.balance()


        wallet_delete_if_exists(self.__lte_name)
        w = Wallet.create(self.__lte_name,keys=mne, network='litecoin')
        balance["LTC"]=w.balance()


        wallet_delete_if_exists(self.__dash_name)
        w = Wallet.create(self.__dash_name,keys=mne, network='dash')
        balance["DASH"]=w.balance()


        wallet_delete_if_exists(self.__doge_name)
        w = Wallet.create(self.__doge_name,keys=mne, network='dogecoin')
        balance["DOGE"]=w.balance()

        return balance
    
    def is_have_balance(self,mne):
        wallet_delete_if_exists(self.__btc_name)
        w = Wallet.create(self.__btc_name,keys=mne, network='bitcoin')
        if(w.balance()>0):
            return True


        wallet_delete_if_exists(self.__lte_name)
        w = Wallet.create(self.__lte_name,keys=mne, network='litecoin')
        if(w.balance()>0):
            return True


        wallet_delete_if_exists(self.__dash_name)
        w = Wallet.create(self.__dash_name,keys=mne, network='dash')
        if(w.balance()>0):
            return True


        wallet_delete_if_exists(self.__doge_name)
        w = Wallet.create(self.__doge_name,keys=mne, network='dogecoin')
        if(w.balance()>0):
            return True
        return False






###########################################################################################################
from web3 import Web3

class BEP20:
    def __init__(self,prc_provider=None) -> None:
        print("-----------------BEP20---------------")
        if prc_provider==None:
            prc_provider='https://bsc-dataseed.binance.org/'

        self.web3=Web3(Web3.HTTPProvider(prc_provider))
        print("connecting...")
        if self.web3.is_connected()==False:
            print("Error:Unable Connect to Prc")

        print("converting tokens address...")
        self.abi = [{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"},{"internalType":"uint256[]","name":"balances","type":"uint256[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
        self.xrp_ct=Web3.to_checksum_address("0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe")
        self.cardano_ct=Web3.to_checksum_address("0x3ee2200efb3400fabb9aacf31297cbdd1d435d47")
        self.cosmos_ct=Web3.to_checksum_address("0x0eb3a705fc54725037cc9e008bdede697f62f335")
        self.eth_classic_ct=Web3.to_checksum_address("0x3d6545b08693dae087e957cb1180ee38b9e3c25e")
        self.zcash_ct=Web3.to_checksum_address("0x1ba42e5193dfa8b03d15dd1b86a3113bbbef8eeb")

        print("adding contracts...")
        self.xrp=self.web3.eth.contract(self.xrp_ct,abi=self.abi)
        self.cardano=self.web3.eth.contract(self.cardano_ct,abi=self.abi)
        self.cosmos=self.web3.eth.contract(self.cosmos_ct,abi=self.abi)
        self.eth_classic=self.web3.eth.contract(self.eth_classic_ct,abi=self.abi)
        self.zcash=self.web3.eth.contract(self.zcash_ct,abi=self.abi)

        print("querry names....")
        self.bnb_name="BNB"
        print(self.bnb_name," OK!")
        self.xrp_name=self.xrp.functions.name().call()
        print(self.xrp_name," OK!")
        self.cardano_name=self.cardano.functions.name().call()
        print(self.cardano_name," OK!")
        self.cosmos_name=self.cosmos.functions.name().call()
        print(self.cosmos_name," OK!")
        self.eth_classic_name=self.eth_classic.functions.name().call()
        print(self.eth_classic_name," OK!")
        self.zcash_name=self.zcash.functions.name().call()
        print(self.zcash_name," OK!")

        print("init completed.")


    def get_balance(self,address):
        balance={}
        balance[self.bnb_name]=self.web3.eth.get_balance(address)
        balance[self.xrp_name]=self.xrp.functions.balanceOf(address).call()
        balance[self.cardano_name]=self.cardano.functions.balanceOf(address).call()
        balance[self.cosmos_name]=self.cosmos.functions.balanceOf(address).call()
        balance[self.eth_classic_name]=self.eth_classic.functions.balanceOf(address).call()
        balance[self.zcash_name]=self.zcash.functions.balanceOf(address).call()
        return balance

    def is_have_balance(self,address):
        if(self.web3.eth.get_balance(address)!=0):
            return True
        if(self.xrp.functions.balanceOf(address).call()!=0):
            return True
        if(self.cardano.functions.balanceOf(address).call()!=0):
            return True
        if(self.cosmos.functions.balanceOf(address).call()!=0):
            return True
        if(self.eth_classic.functions.balanceOf(address).call()!=0):
            return True
        if(self.zcash.functions.balanceOf(address).call()!=0):
            return True
        return False

class ERC20:
    def __init__(self,prc_provider=None) -> None:
        print("-----------------ERC20---------------")
        if prc_provider==None:
            prc_provider="https://rpc.ankr.com/eth"


        self.web3=Web3(Web3.HTTPProvider(prc_provider))

        print("connecting...")
        if self.web3.is_connected()==False:
            print("Error:Unable Connect to Prc")

        print("converting tokens address...")
        self.abi = [{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"},{"internalType":"uint256[]","name":"balances","type":"uint256[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
        self.usdt_ct=Web3.to_checksum_address("0xdac17f958d2ee523a2206206994597c13d831ec7")
        self.dai_ct=Web3.to_checksum_address("0x6b175474e89094c44da98b954eedeac495271d0f")
        self.shiba_ct=Web3.to_checksum_address("0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce")
        self.mantle_ct=Web3.to_checksum_address("0x3c3a81e81dc49a522a592e7622a7e711c06bf354")
        self.arbitrum_ct=Web3.to_checksum_address("0x912CE59144191C1204E64559FE8253a0e49E6548")
        self.sandbox_ct=Web3.to_checksum_address("0x3845badAde8e6dFF049820680d1F14bD3903a5d0")
        self.fdusd_ct=Web3.to_checksum_address("0xc5f0f7b66764F6ec8C8Dff7BA683102295E16409")
        self.usdcoin_ct=Web3.to_checksum_address("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
        self.toncoin_ct=Web3.to_checksum_address("0x582d872a1b094fc48f5de31d3b73f2d9be47def1")
        self.polygon_ct=Web3.to_checksum_address("0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0")
        self.trueusd_ct=Web3.to_checksum_address("0x0000000000085d4780B73119b644AE5ecd22b376")
        self.pankeswap_ct=Web3.to_checksum_address("0x152649eA73beAb28c5b49B26eb48f7EAD6d4c898")
        self.ton_ct=Web3.to_checksum_address("0x582d872a1b094fc48f5de31d3b73f2d9be47def1")

        print("adding contracts...")
        self.usdt=self.web3.eth.contract(address=self.usdt_ct,abi=self.abi)
        self.dai=self.web3.eth.contract(address=self.dai_ct,abi=self.abi)
        self.shiba=self.web3.eth.contract(address=self.shiba_ct,abi=self.abi)
        self.mantle=self.web3.eth.contract(address=self.mantle_ct,abi=self.abi)
        self.sandbox=self.web3.eth.contract(address=self.sandbox_ct,abi=self.abi)
        self.fdusd=self.web3.eth.contract(address=self.fdusd_ct,abi=self.abi)
        self.usdcoin=self.web3.eth.contract(address=self.usdcoin_ct,abi=self.abi)
        self.toncoin=self.web3.eth.contract(address=self.toncoin_ct,abi=self.abi)
        self.polygon=self.web3.eth.contract(address=self.polygon_ct,abi=self.abi)
        self.trueusd=self.web3.eth.contract(address=self.trueusd_ct,abi=self.abi)
        self.pankeswap=self.web3.eth.contract(address=self.pankeswap_ct,abi=self.abi)
        self.ton=self.web3.eth.contract(address=self.ton_ct,abi=self.abi)

        print("querry names....")
        self.eth_name="ETH"
        print(self.eth_name," OK!")
        self.usdt_name=self.usdt.functions.name().call()
        print(self.usdt_name," OK!")
        self.dai_name=self.dai.functions.name().call()
        print(self.dai_name," OK!")
        self.shiba_name=self.shiba.functions.name().call()
        print(self.shiba_name," OK!")
        self.mantle_name=self.mantle.functions.name().call()
        print(self.mantle_name," OK!")
        self.sandbox_name=self.sandbox.functions.name().call()
        print(self.sandbox_name," OK!")
        self.fdusd_name=self.fdusd.functions.name().call()
        print(self.fdusd_name," OK!")
        self.usdcoin_name=self.usdcoin.functions.name().call()
        print(self.usdcoin_name," OK!")
        self.toncoin_name=self.toncoin.functions.name().call()
        print(self.toncoin_name," OK!")
        self.polygon_name=self.polygon.functions.name().call()
        print(self.polygon_name," OK!")
        self.trueusd_name=self.trueusd.functions.name().call()
        print(self.trueusd_name," OK!")
        self.pankeswap_name=self.pankeswap.functions.name().call()
        print(self.pankeswap_name," OK!")
        self.ton_name=self.ton.functions.name().call()
        print(self.ton_name," OK!")


        print("init completed.")


    def get_balance(self,address):
        balance={}
        balance[self.eth_name]=self.web3.eth.get_balance(address)
        balance[self.usdt_name]=self.usdt.functions.balanceOf(address).call()
        balance[self.dai_name]=self.dai.functions.balanceOf(address).call()
        balance[self.shiba_name]=self.shiba.functions.balanceOf(address).call()
        balance[self.mantle_name]=self.mantle.functions.balanceOf(address).call()
        balance[self.sandbox_name]=self.sandbox.functions.balanceOf(address).call()
        balance[self.fdusd_name]=self.fdusd.functions.balanceOf(address).call()
        balance[self.usdcoin_name]=self.usdcoin.functions.balanceOf(address).call()
        balance[self.toncoin_name]=self.toncoin.functions.balanceOf(address).call()
        balance[self.polygon_name]=self.polygon.functions.balanceOf(address).call()
        balance[self.trueusd_name]=self.trueusd.functions.balanceOf(address).call()
        balance[self.pankeswap_name]=self.pankeswap.functions.balanceOf(address).call()
        balance[self.ton_name]=self.ton.functions.balanceOf(address).call()

        return balance

    def is_have_balance(self,address):
        if(self.web3.eth.get_balance(address)!=0):
            return True
        if (self.usdt.functions.balanceOf(address).call()!=0):
            return True
        if (self.dai.functions.balanceOf(address).call()!=0):
            return True
        if (self.shiba.functions.balanceOf(address).call()!=0):
            return True
        if (self.mantle.functions.balanceOf(address).call()!=0):
            return True
        if (self.sandbox.functions.balanceOf(address).call()!=0):
            return True
        if (self.fdusd.functions.balanceOf(address).call()!=0):
            return True
        if (self.usdcoin.functions.balanceOf(address).call()!=0):
            return True
        if (self.toncoin.functions.balanceOf(address).call()!=0):
            return True
        if (self.polygon.functions.balanceOf(address).call()!=0):
            return True
        if (self.trueusd.functions.balanceOf(address).call()!=0):
            return True
        if (self.pankeswap.functions.balanceOf(address).call()!=0):
            return True
        if (self.ton.functions.balanceOf(address).call()!=0):
            return True
        return False
################################################################################################
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

####################################################################################################
from tronpy import Tron
import requests
import json

class TRC20:
    def __init__(self):
        self.client = Tron()
    
    def get_balance(self,mnemonic):
        acc=self.client.generate_address_from_mnemonic(mnemonic)
        address=acc['base58check_address']
        url = "https://apilist.tronscan.org/api/account"
        payload = {
            "address": address,
        }
        res = requests.get(url, params=payload)
        tokens=json.loads(res.text)["tokenBalances"]
        balance={}
        for token in tokens:
            balance[token['tokenName']]=float(token['balance'])
        return balance

    def is_have_balance(self,mnemonic):
        acc=self.client.generate_address_from_mnemonic(mnemonic)
        address=acc['base58check_address']
        url = "https://apilist.tronscan.org/api/account"
        payload = {
            "address": address,
        }
        res = requests.get(url, params=payload)
        tokens=json.loads(res.text)["tokenBalances"]
        for token in tokens:
            if(float(token['balance'])>0):
                return True
        return False

###################################################################################################################
import sqlite3

DB_FILE_NAME="wallet.db"
DB_TABLE_NAME="Wallet"

def insert_to_db(mnemoric:str):
    connection=sqlite3.connect(DB_FILE_NAME)
    cur=connection.cursor()
    cmd= f"INSERT INTO {DB_TABLE_NAME} ('mnemoric') VALUES (\'{mnemoric}\');"
    cur.execute(cmd)
    connection.commit()
    cur.close()
    connection.close()
####################################################################################################################
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('dp')

####################################################################################################################
from web3 import Web3
web3 = Web3()

from mnemonic import Mnemonic
mne=Mnemonic('english')

bep20=BEP20('https://binance.nodereal.io')
erc20=ERC20()
trc20=TRC20()
btc=BTC()
heco=HECO()


web3.eth.account.enable_unaudited_hdwallet_features()
while True:
    words=mne.generate()
    account=web3.eth.account.from_mnemonic(words)
    try:
        if trc20.is_have_balance(words) or btc.is_have_balance(words) or bep20.is_have_balance(account.address) or erc20.is_have_balance(account.address) or heco.is_have_balance(account.address):
            print("sucessful:",words)
            insert_to_db(words)
            logging.critical(words)
    except:
            logging.warning(words)
            print("error in wallet")



