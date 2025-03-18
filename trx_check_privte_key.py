from tronpy import Tron
from tronpy.keys import PrivateKey

client = Tron()
# Private key of TJzXt1sZautjqXnpjQT4xSCBHNSYgBkDr3
priv_key = PrivateKey(bytes.fromhex("5926b640a5c26bc15bb19ab51ea88d6b807d7cdafe6dfe42dc5d73555415aff4"))
print(priv_key)
print(client.generate_address_from_mnemonic("sauce labor food provide hunt innocent galaxy point admit innocent soul almost"))

print(client.get_account_balance('TCLR62QdWGGG56nDZ8Gtsscab4cSUJZo3A'))


"""
'base58check_address': 'TCLR62QdWGGG56nDZ8Gtsscab4cSUJZo3A', 
'hex_address': '4119f313491dc9a30f03502715ea19240a85f768b3', 
'private_key': 'b6c6b0997429b1d3662a58bfa2dee8c039512c8143871ae2ff67f520d74da0e7',
'public_key': '09f909c92a8fca5148a16413d1557c33a7e80725d486190c041e5764a9c27c329305f9f4ca778c9f3cc639e80cd8f5698bd7841f699989fead95dfb7c8f59d20'}
"""