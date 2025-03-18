from cardano.wallet import Wallet
from cardano.wallet import WalletService
from cardano.backends.walletrest import WalletREST

ws = WalletService(WalletREST(port=8090))
wal = ws.create_wallet(
        name="ws",
        mnemonic="resist render west spin antique wild gossip thing syrup network risk gospel seek drop receive",
        passphrase="",
        )