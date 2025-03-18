from hdwallet.utils import generate_mnemonic


seed=generate_mnemonic(language="english",strength=128)
print(seed)
