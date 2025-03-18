SEED="sauce labor food provide hunt innocent galaxy point admit innocent soul almost"
from hdwallet import HDWallet
from hdwallet.symbols import TRX as SYMBOL

import json

# Initialize Dogecoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
# Get Dogecoin HDWallet from seed
hdwallet.from_mnemonic(mnemonic=SEED)

# Derivation from path
# hdwallet.from_path("m/44'/3'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, hardened=True)
hdwallet.from_index(60, hardened=True)
hdwallet.from_index(0, hardened=True)
hdwallet.from_index(0)
hdwallet.from_index(1)

# Print all Dogecoin HDWallet information's
print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
"""
print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Seed:", hdwallet.seed())
print("Root XPrivate Key:", hdwallet.root_xprivate_key())
print("Root XPublic Key:", hdwallet.root_xpublic_key())
print("XPrivate Key:", hdwallet.xprivate_key())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Semantic:", hdwallet.semantic())
print("Path:", hdwallet.path())
print("Hash:", hdwallet.hash())
print("P2PKH Address:", hdwallet.p2pkh_address())
print("P2SH Address:", hdwallet.p2sh_address())
print("P2WPKH Address:", hdwallet.p2wpkh_address())
print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
print("P2WSH Address:", hdwallet.p2wsh_address())
print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
"""