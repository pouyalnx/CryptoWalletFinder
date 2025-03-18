mnemonic="sauce labor food provide hunt innocent galaxy point admit innocent soul almost"
from hdwallet import HDWallet
from hdwallet.symbols import TRX


hdwallet=HDWallet(TRX)
hdwallet.from_mnemonic(mnemonic)
print(hdwallet.entropy())
print(hdwallet.dumps())
