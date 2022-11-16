from brownie import Fallout, accounts



def main():
  account_one, account_two = accounts[0], accounts[2]

  fallout_contract = Fallout.deploy({
    'from': account_one,
    'gas_price': 50000
  })

  print(fallout_contract)

  fallout_contract.Fal1out({
    'from': account_one, 
    'value': 500,
    'gas_price': 50000
  })
  
  contract_owner = fallout_contract.getOwner()

  print(f"account-one: {account_one} / contract-owner: {contract_owner}")
   



