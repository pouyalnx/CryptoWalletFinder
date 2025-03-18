from bitcoinlib.wallets import Wallet, wallet_delete,wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic

mne = Mnemonic().generate()
BTC_NAME="btcwallet"
wallet_delete_if_exists(BTC_NAME)
w = Wallet.create(BTC_NAME,keys=mne, network='bitcoin')
print(w.balance())

LTE_NAME="ltcwallet"
wallet_delete_if_exists(LTE_NAME)
w = Wallet.create(LTE_NAME,keys=mne, network='litecoin')
print(w.balance())

DASH_NAME="dashwallet"
wallet_delete_if_exists(DASH_NAME)
w = Wallet.create(DASH_NAME,keys=mne, network='dash')
print(w.balance())

DOGE_NAME="dogewallet"
wallet_delete_if_exists(DOGE_NAME)
w = Wallet.create(DOGE_NAME,keys=mne, network='dogecoin')
print(w.balance())

