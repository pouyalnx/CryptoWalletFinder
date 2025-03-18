seed="sauce labor food provide hunt innocent galaxy point admit innocent soul almost"

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional

# Generate english mnemonic words
#MNEMONIC: str = generate_mnemonic(language="english", strength=128)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # "meherett"

# Initialize Ethereum mainnet BIP44HDWalleto
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=seed, language="english", passphrase=PASSPHRASE
)
# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

print("Mnemonic:", bip44_hdwallet.mnemonic())
print("Base HD Path:  m/44'/60'/0'/0/{address_index}", "\n")
