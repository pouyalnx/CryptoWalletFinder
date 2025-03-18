import requests
import json

def get_balance(address):
  url = "https://apilist.tronscan.org/api/account"
  payload = {
      "address": address,
  }
  res = requests.get(url, params=payload)
  
  trc20=json.loads(res.text)["trc20token_balances"]
  trc721=json.loads(res.text)["trc721token_balances"]
  tbalance=json.loads(res.text)["tokenBalances"]
  balance=json.loads(res.text)["balance"]
  balances=json.loads(res.text)["balances"]
  
  print(trc20)
  print(trc721)
  print(tbalance)
  print(balance)
  print(balances)
  
get_balance('TCLR62QdWGGG56nDZ8Gtsscab4cSUJZo3A')

"""


[]
[]
[{'amount': '52.868506', 'tokenPriceInTrx': 1, 'tokenId': '_', 'balance': '52868506', 'tokenName': 'trx', 'tokenDecimal': 6, 'tokenAbbr': 'trx', 'tokenCanShow': 1, 'tokenType': 'trc10', 'vip': False, 'tokenLogo': 'https://static.tronscan.org/production/logo/trx.png'}, {'tokenId': '1004031', 'tokenName': 'DIAMOND', 'owner_address': 'TGBg5JhbMubFoe1B2ZKWQK7z5kpzDpf9QW', 'tokenAbbr': 'LOVE', 'tokenCanShow': 1, 'transferCount': 90506986, 'tokenLogo': 'https://static.tronscan.org/production/upload/logo/1004031.png?t=1621949280327', 'nrOfTokenHolders': 47355473, 'balance': '23177685', 'tokenDecimal': 6, 'tokenType': 'trc10', 'vip': False}, {'tokenId': '1004920', 'tokenName': 'freee.vip', 'owner_address': 'TTTTTTTokxVDSRdD4cfWDWL7Gi7oG7zdG6', 'tokenAbbr': 'freee.vip', 'tokenCanShow': 1, 'transferCount': 19918708, 'tokenLogo': 'https://static.tronscan.org/production/upload/logo/default.png', 'nrOfTokenHolders': 8224251, 'balance': '8888888', 'tokenDecimal': 6, 'tokenType': 'trc10', 'vip': False}, {'tokenId': '1000947', 'tokenName': 'Chocolate', 'owner_address': 'TECTRWywVdykwqHCgsanuL2UyJ8rKvL6kf', 'tokenAbbr': 'CHOC', 'tokenCanShow': 1, 'transferCount': 3716750, 'tokenLogo': 'https://static.tronscan.org/production/upload/logo/1000947.png?t=1652980623861', 'nrOfTokenHolders': 3217917, 'balance': '1087', 'tokenDecimal': 0, 'tokenType': 'trc10', 'vip': False}]
52868506
[{'amount': '52.868506', 'tokenPriceInTrx': 1, 'tokenId': '_', 'balance': '52868506', 'tokenName': 'trx', 'tokenDecimal': 6, 'tokenAbbr': 'trx', 'tokenCanShow': 1, 'tokenType': 'trc10', 'vip': False, 'tokenLogo': 'https://static.tronscan.org/production/logo/trx.png'}, {'tokenId': '1004031', 'tokenName': 'DIAMOND', 'owner_address': 'TGBg5JhbMubFoe1B2ZKWQK7z5kpzDpf9QW', 'tokenAbbr': 'LOVE', 'tokenCanShow': 1, 'transferCount': 90506986, 'tokenLogo': 'https://static.tronscan.org/production/upload/logo/1004031.png?t=1621949280327', 'nrOfTokenHolders': 47355473, 'balance': '23177685', 'tokenDecimal': 6, 'tokenType': 'trc10', 'vip': False}, {'tokenId': '1004920', 'tokenName': 'freee.vip', 'owner_address': 'TTTTTTTokxVDSRdD4cfWDWL7Gi7oG7zdG6', 'tokenAbbr': 'freee.vip', 'tokenCanShow': 1, 'transferCount': 19918708, 'tokenLogo': 'https://static.tronscan.org/production/upload/logo/default.png', 'nrOfTokenHolders': 8224251, 'balance': '8888888', 'tokenDecimal': 6, 'tokenType': 'trc10', 'vip': False}, {'tokenId': '1000947', 'tokenName': 'Chocolate', 'owner_address': 'TECTRWywVdykwqHCgsanuL2UyJ8rKvL6kf', 'tokenAbbr': 'CHOC', 'tokenCanShow': 1, 'transferCount': 3716750, 'tokenLogo': 'https://static.tronscan.org/production/upload/logo/1000947.png?t=1652980623861', 'nrOfTokenHolders': 3217917, 'balance': '1087', 'tokenDecimal': 0, 'tokenType': 'trc10', 'vip': False}]

"""