import sys
from slither import Slither



slither = Slither('CoinTwo.sol')
coin = slither.get_contract_from_name('Coin')[0]

# Iterate over all the contracts
for contract in slither.contracts:
  print(f'Contract: {contract.name}')

  if contract.name == 'Coin':

    for function in contract.functions:
      # For each function, print basic information
      print(f'\t{function.full_name}:')
      print(f'\t\tVisibility: {function.visibility}')
      print(f'\t\tContract: {function.contract}')
      print(f'\t\tModifier: {[m.name for m in function.modifiers]}')
      # if onlyOwner not a modifier for function, flag




