import requests
import json

def get_balance(address, token_symbol):
  url = "https://apilist.tronscan.org/api/account"
  payload = {
      "address": address,
  }
  res = requests.get(url, params=payload)
  print(json.loads(res.text))
  trc20token_balances = json.loads(res.text)["trc20token_balances"]
  token_balance = next((item for item in trc20token_balances if item["symbol"] == token_symbol), None)
  if token_balance == None:
    return 0
  else:
    return int(token_balance["balance"])
  

print(get_balance("TJhkMbdSH4Ggpko9p3mjarErC53RmuiUqP","tron"))