from bitcoinlib.wallets import Wallet, wallet_delete,wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic

passphrase = Mnemonic().generate()
print(passphrase)
w=Wallet.create()
w = Wallet.create(keys=passphrase, network='bitcoin',)
account_btc2 = w.new_account('Account BTC 2')
account_ltc1 = w.new_account('Account LTC', network='litecoin')
w.get_key()
w.get_key(account_btc2.account_id)
w.get_key(account_ltc1.account_id)
w.info()




